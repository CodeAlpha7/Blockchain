pragma solidity >= 0.5.0 < 0.6.0;

/*
 ________  ___  ___  ________  ________  ________  ________  ___  ________      
|\   __  \|\  \|\  \|\_____  \|\_____  \|\   ____\|\   __  \|\  \|\   ___  \    
\ \  \|\ /\ \  \\\  \\|___/  /|\|___/  /\ \  \___|\ \  \|\  \ \  \ \  \\ \  \   
 \ \   __  \ \  \\\  \   /  / /    /  / /\ \  \    \ \  \\\  \ \  \ \  \\ \  \  
  \ \  \|\  \ \  \\\  \ /  /_/__  /  /_/__\ \  \____\ \  \\\  \ \  \ \  \\ \  \ 
   \ \_______\ \_______\\________\\________\ \_______\ \_______\ \__\ \__\\ \__\
    \|_______|\|_______|\|_______|\|_______|\|_______|\|_______|\|__|\|__| \|__|
________  ________  ________  ________   ___  ___      ___ ________  ___          
|\   ____\|\   __  \|\   __  \|\   ___  \|\  \|\  \    /  /|\   __  \|\  \         
\ \  \___|\ \  \|\  \ \  \|\  \ \  \\ \  \ \  \ \  \  /  / | \  \|\  \ \  \        
 \ \  \    \ \   __  \ \   _  _\ \  \\ \  \ \  \ \  \/  / / \ \   __  \ \  \       
  \ \  \____\ \  \ \  \ \  \\  \\ \  \\ \  \ \  \ \    / /   \ \  \ \  \ \  \____  
   \ \_______\ \__\ \__\ \__\\ _\\ \__\\ \__\ \__\ \__/ /     \ \__\ \__\ \_______\
    \|_______|\|__|\|__|\|__|\|__|\|__| \|__|\|__|\|__|/       \|__|\|__|\|_______|
                                                                                                                                                                   
*/

contract Buzzcoin {
    mapping (address => bool) private perm;
    address[95] private users;
    address owner;
    function () external payable {}
    function donate() external payable {}
    constructor() public{
        owner = msg.sender;
users = [0x1421350ab6660421d2EA4e423a52030c9A19010E,
0x0D2909b3fFA791257e22F5127dEd49e2ee09f7B8,
0x2A76f2a48982A34027661884B16DAb321A5C268D,
0x2af601f3C67FE2B3A561265C07407Cbc8B99D9c2,
0x59db7cABE067bC05c03f808EB369d066b7754e65,
0x5e489f2cA3300d5de81C2d0FeEE4E63078cdE54d,
0x17907F7462527800De43bEFd76b14b2735B1320E,
0xF4ecd62FD10E8fA79aEe688Cb21e7BB7f843e0B3,
0x93A14D2E28f9C352E45133b7ef3bB9E16418fB38,
0xd555E0C45C48c2b38B674CBc6DddF88140bC35a2,
0x9EeD447A7583882DB311f923e0Cd80788E04F7B8,
0x15D3F5032Ee8d70a0FBa32AdB609A6B9cf744C50,
0xa60e2c0ced3322b4170ED197d3A81e5Da7536c5c,
0x7fFE6bBFedef34E4faA8C165c143Bb93BE15C8D6,
0xD35B1d1210676f42096fea8560C2242245B88749,
0x5B9f0091F221738fBb081a8EA7C11615358191F6,
0x857b74780A639A13999b9736c5cB19AD15cF67a9,
0x319ad58C7119E4706Df105acf3015Ef11969Ce8F,
0xA48366294E007e6CaBF5Ef51e7908b5Cda86B649,
0x07349131b620c6b73EcF674b4Ad2b7e1703E2DA4,
0xc0D4669D916034F7bf7965Dc7Df967DB1b7Bc711,
0xB5ed0a50E01a27bEaB8d49d521B2F7F6BCbE7000,
0x52f7fDd5D35182f3553bbd74ED08DC1D628dFA4E,
0xE547ec9BEE4e6c10bf08F3CaeB0b8EA5C65C7D4a,
0xCa15814ec46EAc83b830F55d4eC2910d8ad1f131,
0x43B5fCeB9a97e41B3a906E6886ade6d1d6adADb7,
0x6b041cd044FCd676a2D1AFD8609eb8398E288280,
0xDE0A98283d5De6F1c076cBbabEEE0CbC14CE3385,
0xe5567d93687825aa3514C6Ab67bE778405F34Dc0,
0xd827b46f22aDC76ec3D8D5EF3Feb8ccdbeE1eb5C,
0x1a670964Fb080fAe2f626e5787bE26B7cAAD429b,
0xC78975304075b718afdaa206170C4E71C397caF4,
0xD18Ff98c2172bDdc221Dd789ae0fc5d45d5Cea0B,
0x8d88a3F6082865ff7ae0A10bF58d1618A5161652,
0x0484d8284fE40622B2F5B9cF009778fd954795B2,
0x17ce8932E45dc4fe6Ef573829d0D506b679e24F4,
0xe45F75C32D0eF49c815D4Dc7091FcC9Bb50f5381,
0x86339bDE5F7b2858d1B3599996b39C31fcaf10e4,
0xC5A6b24b55656b78E9c490934808DFC00aB55A35,
0x7d6F87EC611EDE0791fDd71EA876495E36982C20,
0x9f207558cB355619dA5b3bd208AD74D230d04719,
0x7CB70F67CF53388EB79A3b52615C10e049E12026,
0x9267e3Adc2B2cE2394eC1eF0f3f5E37Faa41fA69,
0x6a9B7db3C53D122d3C35C8886059aec48655338C,
0xA478228CEA754d45bCE062f5e7F080254A948880,
0x4489Bdf35ec1f6D1D1eD0139774227D3C3Df3B40,
0x683620c8b57F8a120aD603462e40aF0fbC32aD09,
0xC87539c0a52c8c27934122F2AD29E8E0b666603E,
0x2911F0797e2A84bCb8e38aae44f184e4E3796804,
0x18721a70bA6e10aeaaD01456eEaB4648D7e181F1,
0xB9B1f5b8E81518c93c3f36215F92296B9a8fB1EC,
0x4CB7f141CCB133d13A7A4D29b7B016a2A971dC7C,
0x481dEB9E5DD4E540aFc8647D803CCC09eB429a3E,
0x378B17EEf980975a3e6B49f65971AC9DA731D864,
0x133cC2b6609B5038E569731bBf51E511D062Cd8a,
0xE4854E944eadAa773912bE08903CFD8754b83dEe,
0x5baFa509aA9B48eE43f451dc3A758E26fb01D95e,
0xDE56d88b1CB731aB0396CfBC5E1e5E4363c1CB90,
0x5C51ccFEB1346EbC49bBdDF7E3B041dE59fA398c,
0x59fE8E2f700eD390B8a3144C00090910A7012d65,
0x9d00e06b65E7502F40865204425E18662E128647,
0x4Bb51fD0f871e4F7730765cAfADDA89e54Dd6d89,
0x3Ed1032075C6EeD83eaa1453225Dd6Fad01002f7,
0xddC7DfE7ABC4eb1143F7555d1F91A79ceFD66EF6,
0xA781afe2Dc3A6734e312d9F5f89C0e96b2B89Dc8,
0x5BD52E36bD2E424B5F682ffb5DF4EDa7138787B6,
0xc4C112B01D0B8ac00684487470f580C6837fa49a,
0x2F57CB11be2B4C951591b1eb5f670D7Df51A53fb,
0x1D95c52ec00fce1c4E86f56a26Df021D96451A90,
0x1b14AC53CA25a7F6Afab7d0815645Ce56865B93F,
0x15B3ee6BDF11a5910767Aa39a68d453088c1D90e,
0x89Cade7C952110568B08d98b0AE8F9e4Ce09F09d,
0x659eD00b2BcdB1825668cFcF68AF8490156430C3,
0xC7c94454b16A9Bd2EEd0f01acCc9dD7d41510248,
0x2e446030945980403363af52f4cC37D4f678D96C,
0xa0EEA13BfACc120b274F263a5EBF2a669Dd7E794,
0x2D2f70d4E000C0817c1c510BAfF3bF1200d0626B,
0x872789885B4f2ff4F698b2520879BB734D8dd185,
0x44b0A55737Dd3A2f379253D0c2119627Bcf97FC9,
0x1aB060FF08Fd9b640a58A6eD979d2DEA3Df7f6eA,
0xD045eB5A2F04421a301e1b47a7ee033F28755dE9,
0xbd2fA68FC3d153F8e626Bd1BC20D89d68Cf2e044];
        for(uint i = 0; i < users.length; i++){
            perm[users[i]] = true;
        }
    }

/*
"Ho ho ho wizard noises. If you can guess the number, you win a prize <|:)"
            ,    _
           /|   | |
         _/_\_  >_<
        .-\-/.   |
       /  | | \_ |
       \ \| |\__(/
       /(`---')  |
      / /     \  |
   _.'  \'-'  /  |
   `----'`=-='   '

*/
    mapping (address => uint) gtm;
    function guess_the_number(uint nonce) external payable {
        assert(perm[msg.sender]);
        assert(gtm[msg.sender] <= 20);
        assert(msg.value == 1 ether);
        assert(nonce <= 100);
        uint256 temp = uint256(keccak256(abi.encode(msg.sender)));
        temp = uint256(keccak256(abi.encode(temp, block.number)));
        temp = uint256(keccak256(abi.encode(temp, temp)));
        temp = temp % 100;
        if (nonce == temp) {
            gtm[msg.sender]++;
            msg.sender.transfer(5 ether);
        }

    }


/*
Maim your friends

     o      _o
    <|\,/ /` |>
 ___/_>_____<_\___

*/
    mapping (address => uint) duel;
    address payable private p1;
    uint256 private dplays;
    function duel1v1() external payable {
        assert(perm[msg.sender]);
        assert(duel[msg.sender] <= 30);
        assert(msg.value == 1 ether);
        assert(p1 != msg.sender);
        duel[msg.sender]++;
        if(dplays == 0){
            p1 = msg.sender;
            dplays = 1;
        }
        else {
            uint winner =  uint256(keccak256(abi.encode(msg.sender,p1))) %2;
            if(winner == 0){
                msg.sender.transfer(5 ether);
            }
            else {
                p1.transfer(6 ether);
            }
            delete dplays;
            delete p1;
        }
    }


/*
higher stakes :OOO !!

           \ /
       |_O  X  O_\
        /`-/ \-'\
       | \     / |
______/___\____|_\____

*/
    address payable private p1h;
    uint256 dhplays;
    function duel_highroller() external payable {
        assert(perm[msg.sender]);
        assert(duel[msg.sender] <= 30);
        assert(msg.value == 5 ether);
        assert(p1h != msg.sender);
        duel[msg.sender]++;
        if(dhplays == 0){
            p1h = msg.sender;
            dhplays = 1;
        }
        else {
            uint winner =  uint256(keccak256(abi.encode(msg.sender,p1h))) %2;
            if(winner == 0){
                msg.sender.transfer(10 ether);
            }
            else {
                p1h.transfer(12 ether);
            }
            delete dhplays;
            delete p1h;
        }
    }



/*
I will pay you to mine. The faster you can mine, the more you get paid. 
Your speedups will not really come from hardware, but from implmentation
How much faster would this be in a systems language like C++ or Rust? 
What about a GPU solution? Pay off is exponential.

                             ___
                     /======/
            ____    //      \___       ,/
             | \\  //           :,   ./
     |_______|__|_//            ;:; /
    _L_____________\o           ;;;/
____(CCCCCCCCCCCCCC)____________-/_____________

*/
    mapping (address => uint256) previous_max;
     
    function pay_to_mine(uint nonce, uint d) external payable {
    	assert(perm[msg.sender]);
        assert(msg.value == 1 ether);
        assert(d >= 33);
        assert(d > previous_max[msg.sender]);
        uint256 hash = uint256(keccak256(abi.encode(nonce,msg.sender)));
        uint mask = 1<<d;
        if (hash % mask == 0) {
            previous_max[msg.sender] = d;
            uint amt = 1<<(d-33);
            msg.sender.transfer(amt * 10 ** 18);
        }
    }



/*
King of the Hill. Coup the current king by paying them off 
                 
                 |ZZzzz
                 |
                 |
    |ZZzzz      /^\            |ZZzzz
    |          |~~~|           |
    |        |^^^^^^^|        / \
   /^\       |[]+    |       |~~~|
|^^^^^^^|    |    +[]|       |   |
|    +[]|/\/\/\/\^/\/\/\/\/|^^^^^^^|
|+[]+   |~~~~~~~~~~~~~~~~~~|    +[]|
|       |  []   /^\   []   |+[]+   |
|   +[]+|  []  || ||  []   |   +[]+|
|[]+    |      || ||       |[]+    |
|_______|------------------|_______|

*/
    address payable public richest;
    uint256 public most_sent;
    uint256 public coup_block;
    mapping (address => uint256) pending_withdrawals;

    function KOTH_coup() public payable returns (bool) {
        if (msg.value > most_sent) {
            if(coup_block == 0){
                coup_block = block.number;
            }
            pending_withdrawals[richest] += msg.value;
            uint amount = block.number - coup_block;
            amount = amount>>3;
            amount = amount;
            richest.transfer(amount * (1 ether));
            richest = msg.sender;
            coup_block = block.number;
            most_sent = msg.value;
            return true;
        } else {
            return false;
        }
    }
    function KOTH_withdraw() public {
        uint256 amt = pending_withdrawals[msg.sender];
        pending_withdrawals[msg.sender] = 0;
        msg.sender.transfer(amt);
    }


 
/*
https://www.vice.com/en/article/4agdwg/pete-buttigieg-would-really-like-you-to-forget-about-that-wine-cavei
         __             _,-"~^"-.
       _// )      _,-"~`         `.
     ." ( /`"-,-"`                 ;
    / 6                             ;
   /           ,             ,-"     ;
  (,__.--.      \           /        ;
   //'   /`-.\   |          |        `._________
     _.-'_/`  )  )--...,,,___\     \-----------,)
   ((("~` _.-'.-'           __`-.   )         //
         ((("`             (((---~"`         //
                                            ((________________
                                            `----""""~~~~^^^```
*/
    uint256 private plays = 0;
    uint256 private total = 0;
    uint256[101] private counter;
    address payable[101] private identity;
    address payable[5] private already_played;

    mapping (address => uint) mayor;

    function mayor_voting() external payable {
        if(msg.value  % (1 ether) != 0 || msg.value == 0 || msg.value > (100 ether)){
            revert();
        }
        assert(perm[msg.sender]);
        assert(mayor[msg.sender] <= 30);
        uint256 val = msg.value / (1 ether);

        for(uint i = 0; i < 5; i++){
            if(already_played[i] == msg.sender) {
                revert();
            }
        }

        mayor[msg.sender]++;
        already_played[plays] = msg.sender;
        plays++;
        counter[val]++;
        identity[val] = msg.sender;
        total += msg.value;

        if (plays == 5) {
            bool paid = false;
            for (uint i = 0; i < 101; i++) {
                if(counter[i] == 1 && !paid){
                    identity[i].transfer(total + (5 ether));
                    paid = true;
                }
                delete counter[i];
                delete identity[i];
            }
            plays = 0;
            total = 0;

            for (uint i = 0; i < 5; i++)
                delete already_played[i];
        }
    }
}
