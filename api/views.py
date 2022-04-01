from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def times(request):
    """Listar os tempos das infos passadas"""

    # , project_id, user_id, started_at, ended_at
    return Response(
        "Não existe Usuário com ID..",
        status=status.HTTP_400_BAD_REQUEST
    )
    # Requests: { "project_id": INT, "user_id": INT, "started_at": DATETIME, "ended_at": DATETIME, }
    # Return Success: { "time" : OBJECT }
    # Return Fail: { "message" : STRING }
