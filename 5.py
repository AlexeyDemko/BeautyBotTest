import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()

function_mapping = {}


def register_function(func):
    function_mapping[func.__name__] = func
    return func


@register_function
async def function1(data):
    return f"Function 1 executed with data: {data}"


@register_function
async def function2(data):
    return f"Function 2 executed with data: {data}"


@app.post('/Datalore')
async def process_webhook(data: dict):
    try:
        function_name = data.get('function')
        selected_function = function_mapping.get(function_name)

        if selected_function:
            result = await selected_function(data)
            return {'result': result}
        else:
            raise HTTPException(status_code=400, detail='Invalid function name')

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
