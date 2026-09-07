ice_cream_flavors = [
    "Vanilla",
    "Chocolate",
    "Strawberry",
    "Mint Chocolate Chip"
]
for flavor in ice_cream_flavors:
    prompt = f"""
    For the ice cream flavor listed below,
    provide a captivating description
    for promotional purposes.

    Flavor: {flavor}
    """
    prompt=print_llm_response       
    print(prompt)