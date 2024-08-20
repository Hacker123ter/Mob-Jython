from org.bukkit import Bukkit
from org.bukkit.command import CommandExecutor
from org.bukkit.entity import Player
from org.bukkit.entity import Pig, Cow, Sheep
from org.bukkit import Location
import random

class HelloCommand(CommandExecutor):
    def onCommand(self, sender, command, label, args):
        if isinstance(sender, Player):
            player = sender
            mobs = {
                'Pig': Pig,
                'Cow': Cow,
                'Sheep': Sheep
            }
            mob_name, mob_class = random.choice(list(mobs.items()))
            player.sendMessage("You spawned a {}!".format(mob_name))
            location = player.getLocation()
            spawn_location = Location(location.getWorld(), location.getX(), location.getY() + 1, location.getZ())
            spawn_mob(spawn_location, mob_class)
            return True
        else:
            sender.sendMessage(u"\u042D\u0442\u0443 \u043A\u043E\u043C\u0430\u043D\u0434\u0443 \u043C\u043E\u0436\u043D\u043E \u0438\u0441\u043F\u043E\u043B\u044C\u0437\u043E\u0432\u0430\u0442\u044C \u0442\u043E\u043B\u044C\u043A\u043E \u0438\u0433\u0440\u043E\u043A\u0430\u043C!")
            return True

def spawn_mob(location, mob_class):
    mob = location.getWorld().spawn(location, mob_class)
    return mob

def main():
    plugin = Bukkit.getPluginManager().getPlugin("Jython")
    command_executor = HelloCommand()
    plugin.getCommand("hello").setExecutor(command_executor)