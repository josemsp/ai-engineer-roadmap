documents = [
    {
        "id": 1,
        "name": "vacations.pdf",
        "category": "human_resources",
        "chunks": [
            "Employees have 15 vacation days.",
            "Vacation requests require manager approval.",
            "Unused days follow company policy."
        ]
    },
    {
        "id": 2,
        "name": "refunds.pdf",
        "category": "finance",
        "chunks": [
            "Customers can request refunds within 30 days.",
            "Refunds require proof of purchase."
        ]
    },
    {
        "id": 3,
        "name": "security.pdf",
        "category": "technology",
        "chunks": [
            "Passwords must contain at least 12 characters.",
            "Multi-factor authentication is required."
        ]
    }
]

def get_all_chunks(docs):
    all_chunks = []
    
    for doc in docs:
        for chunk in doc["chunks"]:
            all_chunks.append({
                "document_id": doc["id"],
                "document_name": doc["name"],
                "category": doc["category"],
                "content": chunk
            })
    
    return all_chunks

def get_chunks_by_category(documents, category):
    chunks = get_all_chunks(documents)
    
    return [
        chunk
        for chunk in chunks
        if chunk["category"] == category
    ]


def get_unique_categories(documents):    
    return {
        doc["category"]
        for doc in documents
    }


if __name__ == "__main__":
    chunks = get_all_chunks(documents)
    
    print("All chunks:")
    print(chunks)
    
    print("\Human resources chunks:")
    print(get_chunks_by_category(documents, "human_resources"))
    
    print("\nCategories")
    print(get_unique_categories(documents))

        
    # Exercise 1 - remove duplicates
    emails = [
        "ana@example.com",
        "pedro@example.com",
        "ana@example.com",
        "carlos@example.com"
    ]

    def get_unique_emails(emails):
        return {
            email for email in emails
        }

    print(get_unique_emails(emails))


    # exercise 2 - index users
    users = [
        {"id": 1, "name": "Ana"},
        {"id": 2, "name": "Pedro"},
        {"id": 3, "name": "Carlos"}
    ]

    def index_by_id(users):
        return {
            user["id"]: user for user in users
        }

    print(index_by_id(users))

    # exercise 3 - filter documents
    def filter_chunks_by_word(documents, search):
        chunks = get_all_chunks(documents)
        
        return [
            chunk for chunk in chunks if search in chunk["content"].lower()
        ]
    
    print("\nFiltered chunks:")
    print(filter_chunks_by_word(documents, "vacation"))
    
    #exercise 4 - copy objects
    import copy
    document = {
        "name": "manual.pdf",
        "metadata": {
            "category": "finance"
        }
    }

    # new_document = document.copy()
    new_document = copy.deepcopy(document)

    new_document["metadata"]["category"] = "technology"

    print(document)
    # change because copy do a superficial copy, we need a deep copy
    
    