@swag_from({
    "tags": ["Service Tickets"],
    "summary": "Create Service Ticket",
    "security": [
        {
            "Bearer": []
        }
    ],
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "$ref": "#/definitions/ServiceTicketPayload"
            }
        }
    ]
})