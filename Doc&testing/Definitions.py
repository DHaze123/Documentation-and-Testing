template = {
    "swagger": "2.0",
    "info": {
        "title": "Mechanic Shop API",
        "description": "API for managing customers, mechanics, service tickets and inventory",
        "version": "1.0"
    },
    "definitions": {
        "CustomerPayload": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "example": "John Doe"
                },
                "email": {
                    "type": "string",
                    "example": "john@email.com"
                },
                "phone": {
                    "type": "string",
                    "example": "555-1234"
                }
            }
        },

        "CustomerResponse": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer",
                    "example": 1
                },
                "name": {
                    "type": "string",
                    "example": "John Doe"
                },
                "email": {
                    "type": "string",
                    "example": "john@email.com"
                }
            }
        }
    }
}