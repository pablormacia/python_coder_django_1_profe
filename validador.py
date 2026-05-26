# Estados del flujo
tiene_init = False
tiene_feature = False
tiene_commit = False
tiene_requirements = False
tiene_readme = False
tiene_views = False
tiene_template = False
tiene_push = False
tiene_pull_request = False


# Cantidad de eventos
n = int(input())


# Procesar eventos
for _ in range(n):

    linea = input()

    # Separar tipo de evento del resto
    partes = linea.split(maxsplit=1)

    tipo_evento = partes[0]

    detalles = ""

    if len(partes) > 1:
        detalles = partes[1]

    # INIT
    if tipo_evento == "INIT":
        tiene_init = True

    # CREATE_BRANCH
    elif tipo_evento == "CREATE_BRANCH":

        nombre_rama = detalles

        if nombre_rama.startswith("feature"):
            tiene_feature = True

    # COMMIT
    elif tipo_evento == "COMMIT":

        mensaje = detalles.strip()

        if mensaje != "":
            tiene_commit = True

    # CREATE_FILE
    elif tipo_evento == "CREATE_FILE":

        nombre_archivo = detalles

        if nombre_archivo == "requirements.txt":
            tiene_requirements = True

        elif nombre_archivo == "README.md":
            tiene_readme = True

        elif nombre_archivo == "views.py":
            tiene_views = True

        elif nombre_archivo == "template.html":
            tiene_template = True

    # PUSH
    elif tipo_evento == "PUSH":
        tiene_push = True

    # PULL_REQUEST
    elif tipo_evento == "PULL_REQUEST":
        tiene_pull_request = True


# Validación final
if (
    tiene_init
    and tiene_feature
    and tiene_commit
    and tiene_requirements
    and tiene_readme
    and tiene_views
    and tiene_template
    and tiene_push
    and tiene_pull_request
):
    print("VALID")

else:
    print("INVALID")