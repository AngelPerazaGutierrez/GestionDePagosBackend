import uvicorn

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, proxy_headers=True, reload=True)