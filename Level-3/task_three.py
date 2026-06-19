"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
"""


def generate_invoice(receipt_string: str) -> str:
    """Turns a receipt string into a VAT invoice string."""

    lines = receipt_string.strip().split("\n")
    item_lines = [line for line in lines if not line.startswith("Total:")]

    ex_vat_lines = []
    total_ex_vat = 0

    for line in item_lines:
        price = float(line.split("£")[1])
        item_str = line.split(" - ")[0]
        ex_vat = price * 0.8
        total_ex_vat += ex_vat

        ex_vat_lines.append(f"{item_str} - £{ex_vat:.2f}")

    total_inc_vat = float(lines[-1].split("£")[1])
    total_ex_vat = round(total_ex_vat, 2)
    vat = round(total_inc_vat - total_ex_vat, 2)

    receipt_lines = ["VAT RECEIPT", ""]
    if ex_vat_lines:
        receipt_lines.extend(ex_vat_lines)
        receipt_lines.append("")

    receipt_lines.append(f"Total: £{total_ex_vat:.2f}")
    receipt_lines.append(f"VAT: £{vat:.2f}")
    receipt_lines.append(f"Total inc VAT: £{total_inc_vat:.2f}")

    return "\n".join(receipt_lines)


if __name__ == "__main__":
    receipt_string = """Bread x 2 - £3.60
Milk x 1 - £0.80
Butter x 1 - £1.20
Total: £5.60"""
    print(generate_invoice(receipt_string))
