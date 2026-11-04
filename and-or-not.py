# and, or, not example
has_ticket = True
has_pass = False
is_vip = True

can_enter = (has_ticket and has_pass) or is_vip
print("Can enter event:", can_enter)
print("Is regular guest:", not is_vip)