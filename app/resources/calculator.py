from flask_restful import Resource, reqparse
from app.models.stack import Stack

stack = Stack()


class Calculator(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("value", type=float, required=False)

    @staticmethod
    def get():
        """
        Gets the current stack
        """
        print("Calling GET method")
        return {"stack": stack.items, "message": "Stack successfully retrieved"}, 200

    def post(self):
        """Adds an element to the current stack"""
        print("Calling POST method")
        args = self.parser.parse_args()
        value = args["value"]
        if value:
            stack.push(value)
            return {"message": f"{value} has been added to the stack", "stack": stack.items}, 201

    @staticmethod
    def delete():
        """Clears the stack"""
        stack.clear()
        return {"message": "Stack is cleared", "stack": stack.items}, 200

    def put(self, operation):
        print(operation)
        match operation:
            case "add":
                stack.add()
            case "mul", "multiply":
                stack.multiply()
            case "sub", "substract":
                stack.subtract()
            case "div", "divide":
                stack.divide()
            case _:
                return {"message": "Unrecognized operation"}, 400
        return {"stack": stack.items, "message": f"Realized operation {operation}"}, 200

