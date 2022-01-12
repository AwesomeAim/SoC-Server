from server import database
from server.constants import TargetType
from server.exceptions import ClientError, ArgumentError

from . import mod_only

__all__ = [
    "ooc_cmd_disemvowel",
    "ooc_cmd_undisemvowel",
    "ooc_cmd_shake",
    "ooc_cmd_unshake",
    "ooc_cmd_typo",
    "ooc_cmd_untypo",
    "ooc_cmd_formal",
    "ooc_cmd_unformal",
]


@mod_only()
def ooc_cmd_disemvowel(client, arg):
    """
    Remove all vowels from a user's IC chat.
    Usage: /disemvowel <id>
    """
    if len(arg) == 0:
        raise ArgumentError("You must specify a target.")
    try:
        targets = client.server.client_manager.get_targets(
            client, TargetType.ID, int(arg), False
        )
    except:
        raise ArgumentError("You must specify a target. Use /disemvowel <id>.")
    if targets:
        for c in targets:
            database.log_area("disemvowel", client, client.area, target=c)
            c.disemvowel = True
        client.send_ooc(f"Disemvowelled {len(targets)} existing client(s).")
    else:
        client.send_ooc("No targets found.")


@mod_only()
def ooc_cmd_undisemvowel(client, arg):
    """
    Give back the freedom of vowels to a user.
    Usage: /undisemvowel <id>
    """
    if len(arg) == 0:
        raise ArgumentError("You must specify a target.")
    try:
        targets = client.server.client_manager.get_targets(
            client, TargetType.ID, int(arg), False
        )
    except:
        raise ArgumentError("You must specify a target. Use /undisemvowel <id>.")
    if targets:
        for c in targets:
            database.log_area("undisemvowel", client, client.area, target=c)
            c.disemvowel = False
        client.send_ooc(f"Undisemvowelled {len(targets)} existing client(s).")
    else:
        client.send_ooc("No targets found.")


@mod_only()
def ooc_cmd_shake(client, arg):
    """
    Scramble the words in a user's IC chat.
    Usage: /shake <id>
    """
    if len(arg) == 0:
        raise ArgumentError("You must specify a target.")
    try:
        targets = client.server.client_manager.get_targets(
            client, TargetType.ID, int(arg), False
        )
    except:
        raise ArgumentError("You must specify a target. Use /shake <id>.")
    if targets:
        for c in targets:
            database.log_area("shake", client, client.area, target=c)
            c.shaken = True
        client.send_ooc(f"Shook {len(targets)} existing client(s).")
    else:
        client.send_ooc("No targets found.")


@mod_only()
def ooc_cmd_unshake(client, arg):
    """
    Give back the freedom of coherent grammar to a user.
    Usage: /unshake <id>
    """
    if len(arg) == 0:
        raise ArgumentError("You must specify a target.")
<<<<<<< HEAD
    try:
        targets = client.server.client_manager.get_targets(
            client, TargetType.ID, int(arg), False
        )
    except:
        raise ArgumentError("You must specify a target. Use /unshake <id>.")
    if targets:
        for c in targets:
            database.log_area("unshake", client, client.area, target=c)
            c.shaken = False
        client.send_ooc(f"Unshook {len(targets)} existing client(s).")
    else:
        client.send_ooc("No targets found.")

# Added by AwesomeAim	
@mod_only()
def ooc_cmd_typo(client, arg):
    """
    Force a typo in a user's messages.
    Usage: /typo <id>
    """
    if len(arg) == 0:
        raise ArgumentError('You must specify a target.')
=======
>>>>>>> 7356e7886476b70d2b92e8c51c15c88efee3c898
    try:
        targets = client.server.client_manager.get_targets(
            client, TargetType.ID, int(arg), False
        )
    except:
<<<<<<< HEAD
        raise ArgumentError('You must specify a target. Use /typo <id>.')
    if targets:
        for c in targets:
            database.log_area('typo', client, client.area, target=c)
            c.typo = True
        client.send_ooc(f'Typo\'d {len(targets)} existing client(s).')
    else:
        client.send_ooc('No targets found.')


@mod_only()
def ooc_cmd_untypo(client, arg):
    """
    Allow the user to make their own typos again.
    Usage: /untypo <id>
    """
    if len(arg) == 0:
        raise ArgumentError('You must specify a target.')
    try:
        targets = client.server.client_manager.get_targets(
            client, TargetType.ID, int(arg), False)
    except:
        raise ArgumentError('You must specify a target. Use /untypo <id>.')
    if targets:
        for c in targets:
            database.log_area('untypo', client, client.area, target=c)
            c.typo = False
        client.send_ooc(f'Untypo\'d {len(targets)} existing client(s).')
    else:
        client.send_ooc('No targets found.')
        
@mod_only()
def ooc_cmd_formal(client, arg):
    """
    Forces the user to speak proper english. Currently expands acronyms.
    Usage: /formal <id>
    """
    if len(arg) == 0:
        raise ArgumentError('You must specify a target.')
    try:
        targets = client.server.client_manager.get_targets(
            client, TargetType.ID, int(arg), False)
    except:
        raise ArgumentError('You must specify a target. Use /formal <id>.')
    if targets:
        for c in targets:
            database.log_area('formal', client, client.area, target=c)
            c.formal = True
        client.send_ooc(f'Made {len(targets)} existing client(s) formal.')
    else:
        client.send_ooc('No targets found.')


@mod_only()
def ooc_cmd_unformal(client, arg):
    """
    Allow the user the freedom of lazy speech.
    Usage: /untypo <id>
    """
    if len(arg) == 0:
        raise ArgumentError('You must specify a target.')
    try:
        targets = client.server.client_manager.get_targets(
            client, TargetType.ID, int(arg), False)
    except:
        raise ArgumentError('You must specify a target. Use /unformal <id>.')
    if targets:
        for c in targets:
            database.log_area('unformal', client, client.area, target=c)
            c.formal = False
        client.send_ooc(f'Allowed {len(targets)} existing client(s) to be not formal.')
=======
        raise ArgumentError("You must specify a target. Use /unshake <id>.")
    if targets:
        for c in targets:
            database.log_area("unshake", client, client.area, target=c)
            c.shaken = False
        client.send_ooc(f"Unshook {len(targets)} existing client(s).")
>>>>>>> 7356e7886476b70d2b92e8c51c15c88efee3c898
    else:
        client.send_ooc("No targets found.")
