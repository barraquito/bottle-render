from bottle import run, get


@get('/')  # our python function based endpoint
def main():
    return "Hello, world!"


if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True)
