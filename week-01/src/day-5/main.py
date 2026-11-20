from document_service import DocumentService

service = DocumentService()

document = service.create_document(
    document_id=1,
    name="vacation.pdf",
    category="human_resources",
    content="Employees have 15 vacation days."
)

print("Created document:")
print(document)

service.process_document(1)

print("\nProcessed document:")
print(service.get_document(1))

print("\nAll documents:")
print(service.get_all_documents())


from product import Product

print("Product")
product1 = Product(1, "Coca", 7.5, 5)
product2 = Product(2, "Pepsi", 7.5, 0)
# product2.update_stock(-1)
print(product1)
print(product2)

