experience:
1. guess the number:
Thought of the logic that I can run the hash logic locally since I already know the message.sender and am able to access block number. First had an issue which took me almost 3 hours to figure out. This was that we cannot use the same nonce for both creating the transaction and calling the function. I needed 2 different transactions and I learned that the long way. Because of this, my transaction would be created, signed and sent but never got back a receipt and the transaction always timedout. Initial rememedies were code corrections, probable traffic on the network so increased gas and gas price to no avail. Then increased timeout duration to almost 10 minutes, none of which worked.

Finally, resolved this issue only for my nonces to be wrong. The only thing I can think of is that msg.sender does not correspond to my public address.

2 days later and testing with local contract deployments, connecting to buzzcoin contract from remix and asking questions on piazza I realized that msg.sender indeed corresponds to public key and the casing of characters does not matter at all. I was looking at the wrong place. Instead my block number was always wrong due to network delays. From the time I calculated the nonce and sent the transaction to when it was actually committed onto the blockchain, the block number would change invalidating my guess. So, I simply incremented by block number by 1 before calculating my guess nonce. I also increased my gas price and gas limit of my transaction so it would be the first to be picked up. This approach worked 18/20 times, with requiring only 2 retries.


2. duel 1v1
Simply called the function with 1 ether, similar to problem 4 of project 1. This deducted 1 ether and did nothing. So, I assumed I lost. Called the function again only for nothing to happen. My deduction was that the function was still waiting for player 2 to participate. After a while, my account was deducted with 2 more coins, I have no idea why. 1 of those coins may have been the earlier function calls, but it still does not explain why an extra coin also disappeared.

