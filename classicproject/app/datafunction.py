from .models import Quotation, Product, Section, Subsection


def grandtotal(sections):
    gt = 0
    print("No of Sections : ", len(sections))
    for s in sections:
        print("Section id , Name ", s.id, " ", s.name)
        try:
            pds = Section.objects.filter(id=s.id).values('product__selling_price')
            for pd in pds:
                print("Price : ", pd["product__selling_price"])
                gt = gt + pd["product__selling_price"]
        except:
            pass
    print("Section Grant Total : ", gt)

    for s in sections:
        try:
            subs = Subsection.objects.filter(section=s.id)
            print("No of Subsections : ", len(subs))
            for sub in subs:
                print("Sub Section id , Name ", sub.id, " ", sub.name)
                try:
                    pds = Subsection.objects.filter(id=sub.id).values('product__selling_price')
                    for pd in pds:
                        print("Price : ", pd["product__selling_price"])
                        gt = gt + pd["product__selling_price"]
                except:
                    pass
        except:
            pass
    print("Grand Total : ", gt)
    return gt


def sectionSubProduct(sections):
    data = []
    for s in sections:
        section = {}
        section['id'] = s.id
        section['name'] = s.name
        section['quotation'] = s.quotation.id
        sprodts = []
        pds = Section.objects.filter(id=s.id).values('product')
        # print("PDS", pds)
        for p in pds:
            prod = Product.objects.get(id=p["product"])
            pdict = {}
            pdict["id"] = prod.id
            pdict["name"] = prod.name
            pdict["description"] = prod.description
            pdict["quantity"] = prod.quantity
            pdict["selling_price"] = prod.selling_price
            sprodts.append(pdict)
        # print("PPPPP", prodts)
        section['sprodts'] = sprodts

        subsectns = []
        subs = Subsection.objects.filter(section=s.id)
        for sub in subs:
            subsection = {}
            subsection['id'] = sub.id
            subsection['name'] = sub.name
            print("SUB name    ", sub.name)
            subprodts = []
            pds = Subsection.objects.filter(id=sub.id).values('product')
            # print("PDS", pds)
            for p in pds:
                prod = Product.objects.get(id=p["product"])
                pdict = {}
                pdict["id"] = prod.id
                pdict["name"] = prod.name
                pdict["description"] = prod.description
                pdict["quantity"] = prod.quantity
                pdict["selling_price"] = prod.selling_price
                subprodts.append(pdict)
            # print("PPPPP", prodts)
            subsection['subprodts'] = subprodts
            subsectns.append(subsection)
        section['subsectns'] = subsectns

        data.append(section)
    return data

