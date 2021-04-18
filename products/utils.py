import tempfile
import shutil
from payment_test.settings import MEDIA_ROOT

def handle_uploaded_file(source):
    fd, filepath = tempfile.mkstemp(prefix=source.name, dir=MEDIA_ROOT)
    with open(filepath, 'wb') as dest:
        shutil.copyfileobj(source, dest)
    return filepath