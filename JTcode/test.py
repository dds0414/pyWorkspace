from recommend import critics
from recommend import sim_distance
from recommend import sim_pearson
from recommend import topMatches
from recommend import getRecommendations
import feedparser


# print sim_distance(critics, "Lisa Rose", "Gene Seymour")
# print sim_pearson(critics, "Lisa Rose", "Gene Seymour")
# print topMatches(critics, "Lisa Rose")
print getRecommendations(critics, "Toby")
# print critics