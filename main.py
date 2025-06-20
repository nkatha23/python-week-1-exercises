import random
import string
from typing import Union, Tuple, List, Dict

# Name Assignment (variables and constants)
MINING_REWARD = 3.125 # Assign the current bitcoin mining reward
current_block_height = 901380 # Assign the current block height as an integer
BTC_TO_SATS = 100_000_000 # Assign the number of satoshis in one Bitcoin

# Functions
def calculate_total_reward(blocks_mined) -> int:
    """Calculate the total Bitcoin reward for a given number of mined blocks.
    
    Args:
        blocks_mined: Number of mined blocks
        
    Returns:
        Total BTC reward
    """
    # Multiply blocks_mined by MINING_REWARD and return result

    return blocks_mined * MINING_REWARD


def is_valid_tx_fee(fee):
    """Return True if the transaction fee is within an acceptable range.
    
    Args:
        fee: Transaction fee in BTC
        
    Returns:
        Boolean indicating whether the fee is valid
    """
    # Check if fee is between 0.00001 and 0.01 BTC

    return 0.00001 <= fee <= 0.01


def is_large_balance(balance):
    """Determine if a wallet balance is considered large.
    
    Args:
        balance: Wallet balance in BTC
        
    Returns:
        True if balance > 50.0 BTC, False otherwise
    """
    # Compare balance to 50.0 and return result

    return balance > 50


def tx_priority(size_bytes, fee_btc):
    """Return the priority of a transaction based on fee rate.
    
    Args:
        size_bytes: Size of transaction in bytes
        fee_btc: Fee of the transaction in BTC
        
    Returns:
        'high' - 0.00005, 'medium' - 0.00001, or 'low' based on fee rate
    """
    # Calculate fee rate and use if-elif-else to determine priority

    fee_rate = fee_btc / size_bytes

    if fee_rate >= 0.00005:
        return 'high'
    elif fee_rate >= 0.00001:
        return 'medium'
    else: 
        return 'low'
    


def is_mainnet(address_type:str):
    """Check if the address type is for Bitcoin mainnet.
    
    Args:
        address_type: String like 'mainnet' or 'testnet'
        
    Returns:
        True if mainnet, False otherwise
    """
    # Convert address_type to lowercase and compare with "mainnet"

    return address_type.upper() == "MAINNET" 



def is_in_range(value):
    """Check if a value is within the range 100 to 200 (inclusive).
    
    Args:
        value: Numeric value
        
    Returns:
        True if in range, else False
    """
    # Use comparison chaining to check if 100 <= value <= 200

    return 100 <= value <= 200


def is_same_wallet(wallet1, wallet2):
    """Check if two wallet objects are the same in memory.
    
    Args:
        wallet1: First wallet object
        wallet2: Second wallet object
        
    Returns:
        True if both point to the same object, else False
    """
    #  Use the 'is' keyword to compare object identity

    return (wallet1 is wallet2)


def normalize_address(address:str):
    """Normalize a Bitcoin address by stripping whitespace and converting to lowercase.
    
    Args:
        address: Raw address string
        
    Returns:
        Normalized address string
    """
    # Strip leading/trailing spaces and convert to lowercase
    return address.strip().lower()


def add_utxo(utxos:list, new_utxo):
    """Add a new UTXO to the list of UTXOs.
    
    Args:
        utxos: List of current UTXOs
        new_utxo: UTXO to add
        
    Returns:
        Updated list of UTXOs
    """
    # Append new_utxo to the utxos list and return it
    utxos.append(new_utxo)

    return utxos



def find_high_fee(fee_list:list):
    """Find the first transaction with a fee greater than 0.005 BTC.
    
    Args:
        fee_list: List of transaction fees
        
    Returns:
        Tuple of (index, fee) or None if not found
    """
    # Use a for loop with enumerate to find fee > 0.005 and return index and value

    for index, fee  in enumerate(fee_list):
        if fee > 0.005:
            return (index, fee)
        
    return None


def get_wallet_details():
    """Return basic wallet details as a tuple.
    
    Returns:
        Tuple containing (wallet_name, balance)
    """
    # Return a tuple with wallet name and balance

    wallet_name = "satoshi_wallet"
    balance = 50.0 
    return (wallet_name, balance)


def get_tx_status(tx_pool: dict, txid:str):
    """Get the status of a transaction from the mempool.
    
    Args:
        tx_pool: Dictionary of txid -> status
        txid: Transaction ID to check
        
    Returns:
        Status string or 'not found'
    """
    # Use dict.get() to return tx status or 'not found' if missing

    return 'confirmed' if tx_pool.get(txid) else 'not found'


def unpack_wallet_info(wallet_info: tuple):
    """Unpack wallet information from a tuple and return a formatted string.
    
    Args:
        wallet_info: Tuple of (wallet_name, balance)
        
    Returns:
        Formatted string of wallet status
    """
    # Unpack wallet_info tuple into name and balance, then format the return string
    wallet_name, balance = wallet_info
    return f"Wallet {wallet_name} has balance: {balance} BTC"

def calculate_sats(btc: float) -> int:
    """Convert BTC to satoshis (1 BTC = 100,000,000 sats).
    
    Args:
        btc: Amount in Bitcoin
        
    Returns:
        Equivalent amount in satoshis
    """
    # Multiply btc by BTC_TO_SATS and return the integer value

    return round( btc * BTC_TO_SATS)


def generate_address(prefix: str = "bc1q") -> str:
    """Generate a mock Bitcoin address with given prefix.
    
    Args:
        prefix: Address prefix (default is bech32)
        
    Returns:
        Mock address string
    """
    # Generate a suffix of random alphanumeric characters (length = 32 - len(prefix))
    prefix = prefix.lower()
    length = 32 - len(prefix)
    valid_prefixes = {"bc1q", "tb1q", "sb1q"}
    if prefix not in valid_prefixes:
        raise ValueError(f"Invalid prefix. Must be one of {valid_prefixes}")
    chars = string.ascii_lowercase + string.digits
    suffix = ''.join(random.choices(chars, k=length))
    # Concatenate the prefix and suffix to form the mock address

    return f"{prefix}{suffix}"


def validate_block_height(height: Union[int, float, str]) -> Tuple[bool, str]:
    """Validate a Bitcoin block height.
    
    Args:
        height: Block height to validate
        
    Returns:
        Tuple of (is_valid, message)
    """
    # Ensure height is an integer
    if not isinstance(height, (int, float, str)):
        return False, "Invalid input type. Must be int, float, or string."
    if isinstance(height, str):
        if height.isdigit():
            return (False, "Block height must be an integer")
        try:
            height = int(height)
        except ValueError:
            return (False, "Unable to convert string to integer block height.")

    elif isinstance(height, float):
        if not height.is_integer():
            return (False, "Block height must be an integer")
        height = int(height)
    # Check that height is not negative
    if height < 0:
        return (False, "Block height cannot be negative")
    # Check that height is within a realistic range (e.g., <= 800,000)
    current_max_block_height = 800_000
    if height > current_max_block_height:
        return (False, f"Block height seems unrealistic")

    return (True, "Valid block height")



def halving_schedule(blocks: List[int]) -> Dict[int, int]:
    """Calculate block reward for given block heights based on halving schedule.
    
    Args:
        blocks: List of block heights
        
    Returns:
        Dictionary mapping block heights to their block reward in satoshis
    """
    # Initialize the base reward in sats
    base_reward = 50
    # Iterate through each block height, compute halvings, and calculate reward
    halving_interval = 210_000
    # Store results in a dictionary
    result = {}


    for height in blocks:
        if height < 0:
            result[height] = -1  # Error code or handle invalid input
            continue

        # Calculate number of halvings: floor((height) / HALVING_INTERVAL)
        halvings = height // halving_interval
        # Cap the number of halvings to prevent reward from going negative
        if halvings >= 64:  # 50 / (2 ** 64) is effectively 0
            reward = 0
        else:
            # Compute reward: base_reward / 2^halvings
            reward = base_reward / (2 ** halvings)

        reward_sats = int(reward * BTC_TO_SATS)
        result[height] = reward_sats
    
    return result


def find_utxo_with_min_value(utxos: List[Dict[str, int]], target: int) -> Dict[str, int]:
    """Find the UTXO with minimum value that meets or exceeds target.
    
    Args:
        utxos: List of UTXOs (each with 'value' key in sats)
        target: Minimum target value in sats
        
    Returns:
        UTXO with smallest value >= target, or empty dict if none found
    """
    # Filter UTXOs to those with value >= target
    candidates = [u for u in utxos if u.get("value", 0) >= target]
    
    # Return the one with the smallest value, or {} if none found
    return min(candidates, key=lambda u: u["value"]) if candidates else {}


def create_utxo(txid: str, vout: int, **kwargs) -> Dict[str, Union[str, int]]:
    """Create a UTXO dictionary with optional additional fields."""
    # Create a base dictionary with txid and vout
    utxo = { "txid": txid, "vout": vout}
    # Merge any extra keyword arguments into the base

    utxo.update(kwargs)

    return utxo


