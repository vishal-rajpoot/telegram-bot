const TelegramBot = require('node-telegram-bot-api');
const cron = require('node-cron');

const botToken = '6234737963:AAF84w6FMwsSOrKO4aMW1yedqnoe_jAQ3aE';
const CHANNEL_ID = 1001910479831; // Replace with your channel's username

const bot = new TelegramBot(botToken, { polling: false });

cron.schedule('*/5 * * * *', async () => {
  try {
    const newInviteLink = await bot.exportChatInviteLink(CHANNEL_ID);
    console.log(`New link: ${newInviteLink}`);
  } catch (error) {
    console.error(`An error occurred: ${error}`);
  }
});
