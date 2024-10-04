echo "BUILD STARTING..."
export PATH=$PATH:/python312/bin
python3 -m pip install django
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput --clear
echo "BUILD END"