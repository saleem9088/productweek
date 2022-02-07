import time

from Page_Object.Pages.HomePage import Home


class Test_Shopping:

    homeNew = Home()
    # checking Temparature
    homeNew.get_url_operation("https://weathershopper.pythonanywhere.com/", homeNew.Current_Temperature)
    homeNew.click_operation(homeNew.Get_Info)
    # Getting Info on what to be purchased
    info = homeNew.get_attribute_value(homeNew.Get_info_text, 'data-content')
    temp = homeNew.get_text_from_locator(homeNew.Current_Temperature)
    res = [int(i) for i in info.split() if i.isdigit()]
    res1 = [int(i) for i in temp.split() if i.isdigit()]
    # Deciding to buy suncreen or moisturizer based on temparature

    if res1[0] < res[0]:
        homeNew.click_operation(homeNew.Get_Moisturizers)

    else:
        homeNew.click_operation(homeNew.Get_Sunscreen)
    p = homeNew.items_to_dictonary(homeNew.Fetch_Product)
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
    homeNew.set_tem(temp)
    homeNew.click_operation(homeNew.Add_product)

    #
    try:
        time.sleep(7)
        dictnaryNew = {}
        for m in p:
            strrNew = m
            if 'SPF-50' in strrNew or 'Almond' in strrNew or 'spf-50' in strrNew:
                dictnaryNew[i] = str(p[i])[1:-1]

        print(dictnaryNew)

        temp1 = min(dictnaryNew.values())
        print(temp1)
        for l in dictnaryNew:
            if temp1 == dictnary[l]:
                temp1 = l
                break
        print(temp1)
        homeNew.set_tem(temp1)
        homeNew.click_operation(homeNew.Add_product)

    except Exception as e:
        print(e)

    #Going to cart and completing payment
    homeNew.click_operation(homeNew.Go_To_Cart)
    homeNew.click_operation(homeNew.Pay_with_Card)
    homeNew.switch_between_frame("stripe_checkout_app")
    homeNew.send_keys_operation(homeNew.Email,"anb@gmail.com")
    homeNew.send_keys_operation(homeNew.Card_Number,"4000056655665556")
    homeNew.send_keys_operation(homeNew.CV, "5565")
    homeNew.send_keys_operation(homeNew.MonthYear, "11")
    time.sleep(5)
    homeNew.send_keys_operation(homeNew.MonthYear, "2022")
    homeNew.send_keys_operation(homeNew.ZIP,"9667")
    homeNew.click_operation(homeNew.Pay_IN_INR)
    time.sleep(6)
    msg=homeNew.get_text_from_locator(homeNew.Success_Msg)
    assert msg == "Your payment was successful. You should receive a follow-up call from our sales team."





