from app.__init__ import create_app

app = create_app('__main__')

app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)