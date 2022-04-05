import discord
from discord import app_commands
from discord.ui import Modal, View, text_input
from discord.ext import tasks

intents = discord.Intents.default()
client = discord.Client(intents=intents)

tree = app_commands.CommandTree(client)


TEST_GUILD = discord.Object(your guild_id)

@tasks.loop(seconds=5)
async def loop():
    await tree.sync(guild=TEST_GUILD)
@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')
    loop.start()
    await tree.sync(guild=TEST_GUILD)

class M(Modal):
    a = text_input.TextInput(label='a', placeholder='a', max_length=20, required=True)
    b = text_input.TextInput(label='b', style=discord.TextStyle.paragraph, required=True)

    def __init__(self):
        super().__init__(title='Test')

    async def on_submit(self, interaction:discord.Interaction):
        await interaction.response.send_message(f'{interaction.user}\n{self.a.value}\n{self.b.value}')
class Button(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(V())

class V(discord.ui.Button):
    def __init__(self):
        super().__init__(label="a",style=discord.ButtonStyle.red)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(M())



@tree.command(guild=TEST_GUILD, description="test")
async def test(interaction: discord.Interaction):
    # Send the modal with an instance of our `Feedback` class
    await interaction.response.send_message(view=Button())

client.run(token)
