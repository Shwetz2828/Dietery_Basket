import base64
from app import create_app

# Encode the secret key using base64
SECRET_KEY = base64.b64encode(b'\xda7=\xbfA\xca\x92\x15\xad\x0f\xffd!\x86\xb5_^\x16\xeb\x8a\x0ep\x19\xa2').decode('utf-8')

app = create_app(secret_key=SECRET_KEY)

if __name__ == '__main__':
    app.run(debug=True)
