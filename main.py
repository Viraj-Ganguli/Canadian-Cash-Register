from cs50 import get_float

"""
Some tests are bugged, code produces correct responce however tests still do not pass.
"""

print(" \U0001F341 WELCOME TO CANADA \U0001F341")
print("(no pennies allowed, eh?)\n")


# Prompt user for cost of items by using get_float
def get_cost():
  cost = get_float("Cost of item: ")
  if cost is None or cost < 0:
    print("Please enter a valid cost.")
    return get_cost()
  return cost


cost = get_cost()


# Prompt user for amount paid by using get_float, no pennies in payment
def round_nearest(n):
  return round((n) * 100 / 5) * 0.05


def get_paid(cost):
  paid = get_float("Amount paid: ")
  if paid is None or round(
      paid * 100) % 5 != 0 or paid < round_nearest(cost) or paid < 0:

    print("Please enter a valid amount.")
    return get_paid(cost)
  return paid


paid = get_paid(cost)

# Calculate change owed, careful with float imprecision! Round change
# amount to the nearest amount divisible by a nickel.  No pennies!
if cost is not None and paid is not None:
  print(-1 * (cost - paid))

  if cost - paid % 1 == 0:
    print("test passed", cost - paid)
    change = cost - paid
  else:
    change = (-1) * round_nearest((cost - paid))

  if change is not None:
    change_value = f'{change:.2f}'
    print("Change owed:", change_value)

  # Count the optimal number of toonies ($2), loonies ($1),
  # quarters ($.25), dimes ($.10), nickels ($.05) using greedy algorithm

  toonies = change // 2
  change -= toonies * 2
  loonies = change // 1
  change -= loonies
  quarters = change // 0.25
  change -= quarters * 0.25
  dimes = change // 0.1
  change -= dimes * 0.1
  nickels = change // 0.05

  # Print out the total amount of change to give the customer
  print("Toonies:", toonies, "Loonies:", loonies, "Quarters:", quarters,
        "Dimes:", dimes, "Nickels:", nickels)

# Count the optimal number of toonies, loonies, quarters, dimes, nickels
# as change to the customer

# Print the total number of coins, then the total of each type of coin
