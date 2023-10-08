pragma solidity 0.8.20;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ClothingItem is ERC721, Ownable {

    uint256 brandID;
    uint256 sewedDate;


    constructor(address _initialAddress, uint256 _brandID, uint256 _sewedDate) ERC721("ClothingItem Token", "CLOTH") Ownable(_initialAddress) { // ERC20("ClothingItem Token", "CLOTH")
        brandID = _brandID;
        sewedDate = _sewedDate;
    }

    struct RefurbishEvent {
        address refurbisher;
        uint256 timestamp;
    }

    RefurbishEvent[] public refurbishmentHistory;
    mapping(address => bool) public verifiedRefurbishers;

    // Function to add a verified refurbisher.
    function addVerifiedRefurbisher(address refurbisher) external {
        require(msg.sender == owner(), "Only the owner can add verified refurbishers");
        verifiedRefurbishers[refurbisher] = true;
    }

    // Private function to record a refurbishment event.
    function _refurbish() private {
        RefurbishEvent memory eventInstance = RefurbishEvent(msg.sender, block.timestamp);
        refurbishmentHistory.push(eventInstance);
    }

    // Public function to initiate refurbishment (can be called by the owner).
    function initiateRefurbishment() external {
        require(verifiedRefurbishers[msg.sender] == true, "To refurbish this item, you have to be verified by the owner.");
        _refurbish();
    }

}
