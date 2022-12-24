from store.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("session_key")
        if "session_key" not in self.session:
            cart = self.session["session_key"] = {}
        self.cart = cart

    def add(self, product, product_qty):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]["qty"] = product_qty
        else:
            self.cart[product_id] = {"price": product.price, "qty": product_qty}
        self.session.modified = True

    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True

    def update(self, product, product_qty):
        product_id = str(product)
        product_quantity = product_qty
        if product_id in self.cart:
            self.cart[product_id]["qty"] = product_quantity
        self.session.modified = True

    def __len__(self):
        return sum(item["qty"] for item in self.cart.values())

    def __iter__(self):
        all_product_ids = self.cart.keys()
        products = dict((str(i.pk), i) for i in Product.objects.filter(id__in=all_product_ids))
        cart = self.cart.copy()

        for key, values in cart.items():
            values["product"] = products.get(key)
            values["total"] = values["price"] * values["qty"]
            yield values

    def get_total(self):
        return sum(item["price"] * item["qty"] for item in self.cart.values())
