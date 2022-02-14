const Discord = require('discord.js');
const { prefix, token } = require('./config.json');

const client = new Discord.Client();

client.on('ready', () => {
	client.user.setActivity(`Splashin ${client.guilds.cache.size} servers`);
	console.log('Potbot online');
});

client.on('message', async message => {

	const args = message.content.slice(prefix.length).trim().split(" | ");
	const command = args.shift().toLowerCase();
	 
	 member = message.author

	if (command == 'splash') {
		if (message.member.roles.cache.some(role => role.name === 'Splasher')) {
		if (args.length < 1) {
            const argsEmbed = new Discord.MessageEmbed()
			  .setColor('#f47fff')
			  .setTitle('Potbot | Proper Usage')
              .setDescription('Follow this example to setup your splash announcement')
              .addField('Example', '-splash | <role to ping> | <party to join/listed hub number> | <splash location> | <additional message>')
              .addField('Permission Requirements:', '"Splasher" role. (this role is cAsE SeNsItIvE)')
	      .addField('Important Information:', 'All the pipes **|** in the command are REQUIRED. any arguments left blank will be read as "undefined"')
			  .setFooter('Message is sent in this channel!')
              message.channel.send(argsEmbed)
              message.channel.send('When you finish your announcement it should look like this.')
            const exampleEmbed = new Discord.MessageEmbed()
            .setColor('#f47fff')
            .setTitle('Potbot | Splash')
            .setDescription('A splasher has pinged you for a splash!')
            .addFields(
                { name: 'How do I get in the splash?', value: '<party to join/listed hub number>'},
                { name: 'Where is the splash?', value: '<splash location>'},
                { name: 'Additional Message from the Splasher', value: '<additional message>'},
                )
        	message.channel.send(exampleEmbed)
		} else {
        var ping = args[0]
        var party = args[1]
        var loc = args[2]
        var note = args[3]
		const splashEmbed = new Discord.MessageEmbed()
            .setColor('#f47fff')
            .setTitle('Potbot | Splash')
            .setDescription('A splasher has pinged you for a splash!')
            .addFields(
                { name: 'How do I get in the splash?', value: `${party}`},
                { name: 'Where is the splash?', value: `${loc}`},
                { name: 'Additional Message from the Splasher', value: `${note}`},
                )
        message.channel.send(`${ping}`)
		message.channel.send(splashEmbed)
		message.delete()
			}
	  }
	 } 
	});

client.login(token);

// we need to make it so that only specific people (splashers) can use the splashall command
// because if anyone were to be able to use it the bot is meant to send ping to every server its in :monkey:
// potential workaround could be two commands one command that sends a splash to all servers and one command that sends locally within the server
// where only defined users can use a splashall command but anyone can use the local splash command

// so yeah i think the plan is we have 2 commands -splash (which is local) and -allsplash which send to all esrver :D
