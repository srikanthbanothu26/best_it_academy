
from app.__init__ import create_app
from dotenv import load_dotenv

load_dotenv()

app = create_app()

if __name__ == "__main__":        
    app.run(debug=False, port=7070) 

