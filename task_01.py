#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 10 synthesizing task 01"""

def sum_orders(customers, orders):
    """This functions combines two datasets into a one.

    Args:
        customers (dict): A dictionary of customers keyed by customer_id
        orders (dict): A dictionary of orders keyed by order id

    Returns:
        It combines two dataset into one dictionary.

    Examples:
        >>> import data
        >>> sum_orders(data.CUSTOMERS, data.ORDERS)
        {1: {'email': 'evorsoisson@komarr.net', 'total': 1287, 'orders': 3, 'name': '
        ''Ekaterin Vorsoisson'}, 2: {'email': 'cordelia@beta.com', 'total': '
        '2778, 'orders': 5, 'name': 'Cordelia Naismith'}, 3: {'email': '
        ''iv398@barrayar.net', 'total': 358, 'orders': 3, 'name': 'Ivan '
        'Vorpatril'}, 4: {'email': 'viceroy@sergyar.net', 'total': 1207, '
        ''orders': 5, 'name': 'Aral Vorkosigan'}, 5: {'email': '
        ''admiral@dendarii.com', 'total': 451, 'orders': 3, 'name': '
        ''Eli Quinn'}, 6: {'email': 'portmaster@graf.net', 'total': 1198, '
        ''orders': 3, 'name': 'Bel Thorne'}, 7: {'email': 'impsec@barrayar.net', '
        ''total': 1897, 'orders': 3, 'name': 'Simon Illyan'}, 8: {'email': '
        ''dg1367@barrayar.net', 'total': 204, 'orders': 1, 'name': '
        ''Duv Galeni'}, 9: {'email': 'impsec@barrayar.net', 'total': 1704, '
        ''orders': 2, 'name': 'Gregor Vorbarra'}}les:
        """
    comb_dict = {}
    orders = orders.values()
    for order in orders:
        key = order['customer_id']
        first_val = customers[key]['name']
        second_val = customers[key]['email']
        if key not in comb_dict.iterkeys():
            third_val = 1
            fourth_val = order['total']
        else:
            third_val = comb_dict[key]['orders'] + 1
            fourth_val = comb_dict[key]['total'] + order['total']
        orderinfor = dict(name=val1, email=val2, orders=val3, total=val4)
        order_customerinfor = {key: orderinfor}
        comb_dict.update(order_customerinfor)
    return comb_dict
