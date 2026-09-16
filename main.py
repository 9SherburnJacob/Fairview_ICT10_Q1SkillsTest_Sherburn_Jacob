from pyscript import display, document


def orderaccept
ish = document.getElementById("amer")
hea = document.getElementById("spain")
sin = document.getElementById("cold")
don = document.getElementById("cappu")
meu = document.getElementById("caramel")

subtotal = (
    (float(ish.value) if ish.checked else 0.0)
    +
    (float(hea.value) if ish.checked else 0.0)
    +
    (float(sin.value) if ish.checked else 0.0)
    +
    (float(don.value) if ish.checked else 0.0)
    +
    (float(meu.value) if ish.checked else 0.0)
    
)

vat = subtotal * 0.12

total = subtotal + vat

display(f"Subtotal: {subtotal}", target="subtote")