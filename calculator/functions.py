def calculate_bonus(completed_deliveries):
    if completed_deliveries > 100:
        bonus = 350
    elif completed_deliveries > 90:
        bonus = 250
    elif completed_deliveries > 80:
        bonus = 220
    elif completed_deliveries > 70:
        bonus = 200
    elif completed_deliveries > 60:
        bonus = 140
    elif completed_deliveries > 50:
        bonus = 120
    elif completed_deliveries > 40:
        bonus = 100
    elif completed_deliveries > 30:
        bonus = 70
    elif completed_deliveries > 20:
        bonus = 45
    else:
        bonus = 0
    return bonus


def total_to_receive(
        completed_deliveries=0,
        delivery_price=0,
        bonus=0,
        collected_money=0,
        tips_on_card=0,
        tips_cash=0,
        company_fixed_commission=0,
        company_percentage_commission=0,
        fuel_cost=0,
        tips_cashed_already=False
):
    if tips_cashed_already:
        tips_cash = -tips_cash
    total = (completed_deliveries * delivery_price + bonus + tips_cash + tips_on_card + collected_money) * \
            (100 - company_percentage_commission) - company_fixed_commission - fuel_cost

    return total
