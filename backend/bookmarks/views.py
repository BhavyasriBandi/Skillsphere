from datetime import datetime, timezone as dt_timezone

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import BookmarkSerializer


# Temporary storage: data is lost when Django restarts.
BOOKMARKS = []
NEXT_BOOKMARK_ID = 1


class BookmarkListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_bookmarks = [
            {
                key: value
                for key, value in bookmark.items()
                if key != "user_id"
            }
            for bookmark in BOOKMARKS
            if bookmark["user_id"] == request.user.id
        ]

        return Response(
            BookmarkSerializer(user_bookmarks, many=True).data
        )

    def post(self, request):
        global NEXT_BOOKMARK_ID

        serializer = BookmarkSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        duplicate = any(
            bookmark["user_id"] == request.user.id
            and bookmark["item_type"] == data["item_type"]
            and bookmark["item_id"] == data["item_id"]
            for bookmark in BOOKMARKS
        )

        if duplicate:
            return Response(
                {"error": "This item is already bookmarked."},
                status=status.HTTP_409_CONFLICT,
            )

        bookmark = {
            "id": NEXT_BOOKMARK_ID,
            "user_id": request.user.id,
            "item_type": data["item_type"],
            "item_id": data["item_id"],
            "title": data.get("title", ""),
            "url": data.get("url", ""),
            "created_at": datetime.now(dt_timezone.utc),
        }

        BOOKMARKS.append(bookmark)
        NEXT_BOOKMARK_ID += 1

        response_data = {
            key: value
            for key, value in bookmark.items()
            if key != "user_id"
        }

        return Response(
            BookmarkSerializer(response_data).data,
            status=status.HTTP_201_CREATED,
        )


class BookmarkDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_bookmark(self, request, bookmark_id):
        return next(
            (
                bookmark
                for bookmark in BOOKMARKS
                if bookmark["id"] == bookmark_id
                and bookmark["user_id"] == request.user.id
            ),
            None,
        )

    def get(self, request, bookmark_id):
        bookmark = self.get_bookmark(request, bookmark_id)

        if bookmark is None:
            return Response(
                {"error": "Bookmark not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        response_data = {
            key: value
            for key, value in bookmark.items()
            if key != "user_id"
        }

        return Response(BookmarkSerializer(response_data).data)

    def delete(self, request, bookmark_id):
        bookmark = self.get_bookmark(request, bookmark_id)

        if bookmark is None:
            return Response(
                {"error": "Bookmark not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        BOOKMARKS.remove(bookmark)

        return Response(
            {"message": "Bookmark removed successfully."},
            status=status.HTTP_200_OK,
        )
