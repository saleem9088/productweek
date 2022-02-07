import time

from Page_Object.Pages.HomePage import Home


class Test_Shopping:
    home1 = Home()
    # checking Temparature
    home1.get_url_operation("https://weathershopper.pythonanywhere.com/", home1.Current_Temperature)
    home1.click_operation(home1.Get_Info)
    # Getting Info on what to be purchased
    info = home1.get_attribute_value(home1.Get_info_text, 'data-content')
    temp = home1.get_text_from_locator(home1.Current_Temperature)
    res = [int(i) for i in info.split() if i.isdigit()]
    res1 = [int(i) for i in temp.split() if i.isdigit()]
    # Deciding to buy suncreen or moisturizer based on temparature

    if res1[0] < res[0]:
        home1.click_operation(home1.Get_Moisturizers)

    else:
        home1.click_operation(home1.Get_Sunscreen)
    p = home1.items_to_dictonary(home1.Fetch_Product)
    print(p)
    # Fetching products containing SPF 30 or Aloe
    dictnary = {}
    for i in p:
        strr = i

        if 'SPF-30' in strr or 'Aloe' in strr or 'spf-30' in strr:
            dictnary[i] = str(p[i])[1:-1]

    print(dictnary)
    temp = min(dictnary.values())
    print(temp)
    # Fetching product with least amount of value
    for k in dictnary:
        if temp == dictnary[k]:
            temp = k
            break
    print(temp)
    home1.set_tem(temp)
    home1.click_operation(home1.Add_product)

    #
    try:
        time.sleep(7)
        dictnary1 = {}
        for m in p:
            strr1 = m
            if 'SPF-50' in strr1 or 'Almond' in strr1 or 'spf-50' in strr1:
                dictnary1[i] = str(p[i])[1:-1]

        print(dictnary1)

        temp1 = min(dictnary1.values())
        print(temp1)
        for l in dictnary1:
            if temp1 == dictnary[l]:
                temp1 = l
                break
        print(temp1)
        home1.set_tem(temp1)
        home1.click_operation(home1.Add_product)

    except Exception as e:
        print(e)

    #Going to cart and completing payment
    home1.click_operation(home1.Go_To_Cart)
    home1.click_operation(home1.Pay_with_Card)
    home1.switch_between_frame("stripe_checkout_app")
    home1.send_keys_operation(home1.Email,"dumm@g.com")
    home1.send_keys_operation(home1.Card_Number,"3622")
    home1.send_keys_operation(home1.CV, "5565")
    time.sleep(5)
    home1.send_keys_operation(home1.Card_Number, "77206")
    home1.send_keys_operation(home1.MonthYear, "11")
    time.sleep(5)
    home1.send_keys_operation(home1.MonthYear, "2032")
    home1.send_keys_operation(home1.Card_Number, "22716")
    home1.send_keys_operation(home1.ZIP,"666767")
    home1.click_operation(home1.Pay_IN_INR)
    time.sleep(6)
    msg=home1.get_text_from_locator(home1.Success_Msg)
    assert msg == "Your payment was successful. You should receive a follow-up call from our sales team."





