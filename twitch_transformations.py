#I am running into issues with the initial data format before compiled it all into a json file.
#So here's the transformations I'm going to show when I work it all out.
#This is from two files. One depicting if streamers are partnered with Twitch and one showing
#when a channel is hosting another channel for extra money and viewers.


#Top 10 games streamed on Twitch
SELECT * Game
FROM twitch_channels
ORDER BY DESC Viewers
LIMIT 10;

#Top 10 streamers on Twitch
SELECT * ID as Streamer
FROM twitch_channels
ORDER BY DESC Viewers
LIMIT 10;

#Number of Partnered Streamers
SELECT COUNT(DISTINCT ID)
FROM twitch_channels
WHERE Partner = True

#Number of partnered channels hosting
SELECT COUNT(DISTINCT hoster)
FROM twitch_hosts
WHERE Partner = True

#Number of channels hosting the top 10 channels
SELECT COUNT(DISTINCT hoster)
FROM twitch_hosts
GROUP BY hostee
LIMIT 10

#Also filter out if the hoster is partnered
SELECT COUNT(DISTINCT hoster)
FROM twitch_hosts
WHERE Partner = True
GROUP BY hostee
LIMIT 10

#Hosts hosting larger channels to boost their audience
SELECT * DISTINCT ID, Viewers
FROM twitch_channels
INNER JOIN twitch_hosts
ON twitch_channels.ID = twitch_hosts.hostee
WHERE twitch_hosts.viewers < twitch_channels.Viewers

#Number of views of top 10 hostees boosted by hoster next to the hostees own viewers
SELECT * DISCTINCT ID, Viewers, SUM(viewers) as hosted_viewers
FROM twitch_channels
INNER JOIN twitch_hosts
ON twitch_channels.ID = twitch_hosts.hostee
GROUP BY twitch_hosts.hostee


#These are just some SQL examples of what this data shows about hosting monetization profits. We can use this to see if hosting
#can help grow a channel and see how much extra money people make from hosting larger channels rather than smaller ones.
#It could pay more to get on the popular bandwagon rather than help grow new upcoming channels.