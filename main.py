from pyscript import display, document



def orderaccept(e)
ish = document.getElementById("amer").innerHTML
hea = document.getElementById("spain").innerHTML
sin = document.getElementById("cold").innerHTML
don = document.getElementById("cappu").innerHTML
meu = document.getElementById("caramel").innerHTML

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

display(f"Subtotal: {subtotal}", target="subtote").innerHTML
display(f"VAT: {vat}", target="tax").innerHTML
display(f"Total: {total}", target="tote").innerHTML