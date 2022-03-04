
load_fixtures="false"
show_help="false"
os_linux="false"
reset_local="false"
run_server="false"
create_superuser="false"

ARGS=$(getopt -a --options fhlrsu --long "fixtures,help,linux,reset,run,superuser" -- "$@")
eval set -- "$ARGS"

while true; do
    case "$1" in
        -f|--fixtures)
            load_fixtures="true"
        shift;;
        -h|--help)
            show_help="true"
        shift;;
        -l|--linux)
            os_linux="true"
        shift;;
        -r|--reset)
            reset_local="true"
        shift;;
        -s|--run)
            run_server="true"
        shift;;
        -u|--superuser)
            create_superuser="true"
        shift;;
        --)
        break;;
        *)
            printf "Unknown option %s\n" "$1"
        exit 1;;
    esac
done

# Show script help
if [ $show_help == true ]; then
    echo "-----------------------------------------------------------------------"
    echo "|  Setup script help                                                  |"
    echo "-----------------------------------------------------------------------"
    echo "   -f |--fixtures  : Load predefined fixtures"
    echo "   -h |--help      : Shows script help"
    echo "   -l |--linux     : Activates virtual environment 'venv' in Linux/ Mac"
    echo "   -r |--reset     : Resets all local environment files and database"
    echo "   -s |--run       : Runs Django web server at the end of script"
    echo "   -u |--superuser : Creates predefined superuser Admin in local"
    echo " "
    exit
fi

# Reset local files and data
if [ $reset_local == true ]; then
    echo "## Reset local files and data"
    rm -rf venv
    rm -rf db.sqlite3
fi

# Export envrionment variables
export SECRET_KEY='your-secret-key'
export STRIPE_PUBLIC_KEY='your-stripe-key'
export STRIPE_SECRET_KEY='sk_test_51KBLl5IVkDFu5crElTmeW0uvV1T2JwktgY9UK8GgCMHmMsWQ5islMY4MEDxfYV7k5qrD58rmxwqQL6UDdILWL4aZ00GIMll7qN'
export EMAIL_HOST_PASS='efuwwviaokoenmne'
export EMAIL_HOST_USER='physioleandro@gmail.com'
export HOST_DOMAIN='http://127.0.0.1:8000'
export DEBUG=True

# Install vritualenv in PIP
pip install virtualenv

# Setup virtual environment locally
virtualenv venv

# Running in Linux / Mac
if [ $os_linux == true ]; then
    echo "## Running venv in Linux / Mac"
    source venv/bin/activate
else
    echo "## Running venv in Windows"
    source venv/Scripts/activate
fi

# Install all application requirements from file
pip install -r requirements.txt

# Make Django database models migrations
python manage.py makemigrations

# Migrate Django database models
python manage.py migrate

# Load apps fixtures
if [ $load_fixtures == true ]; then
    echo "## Load apps fixtures"
    python manage.py loaddata ./services/fixtures/clinicians.json
    python manage.py loaddata ./services/fixtures/services.json
fi

# Create admin superuser
if [ $create_superuser == true ]; then
    echo "## Create admin superuser"
    echo "from django.contrib.auth import get_user_model; CustomUser = get_user_model(); CustomUser.objects.create_superuser('admin', 'physioleandro@gmail.com', 'Admin1234')" | python manage.py shell
fi

# Run local web server
if [ $run_server == true ]; then
    echo "## Run server"
    python manage.py runserver
fi