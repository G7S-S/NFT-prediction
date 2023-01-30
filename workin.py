# OpenRarity version 0.4.0-beta
from open_rarity import (
    Collection,
    Token,
    RarityRanker,
    TokenMetadata,
    StringAttribute,
)
from open_rarity.models.token_identifier import EVMContractTokenIdentifier
from open_rarity.models.token_standard import TokenStandard

# Create OpenRarity collection object and provide all metadata information
collection = Collection(
    name="My Collection Name",
    attributes_frequency_counts={
        "hat": {"cap": 1, "visor": 2},
        "shirt": {"blue": 2, "green": 1},
    },
    tokens=[
        Token(
            token_identifier=EVMContractTokenIdentifier(
                contract_address="0xa3049...", token_id=1
            ),
            token_standard=TokenStandard.ERC721,
            metadata=TokenMetadata(
                string_attributes={
                    "hat": StringAttribute(name="hat", value="cap"),
                    "shirt": StringAttribute(name="shirt", value="blue"),
                }
            ),
        ),
    ],
)  # Replace inputs with your collection-specific details here


# Generate scores for a collection
ranked_tokens = RarityRanker.rank_collection(collection=collection)

# Iterate over the ranked and sorted tokens
for token_rarity in ranked_tokens:
    token_id = token_rarity.token.token_identifier.token_id
    rank = token_rarity.rank
    score = token_rarity.score
    print(f"\tToken {token_id} has rank {rank} score: {score}")
