@customer_bp.route("/", methods=["POST"])
@swag_from({
    "tags": ["Customers"],
    "summary": "Create a new customer",
    "description": "Creates a customer record in the database.",
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "$ref": "#/definitions/CustomerPayload"
            }
        }
    ],
    "responses": {
        201: {
            "description": "Customer created successfully",
            "schema": {
                "$ref": "#/definitions/CustomerResponse"
            }
        },
        400: {
            "description": "Validation Error"
        }
    }
})
def create_customer():
    pass