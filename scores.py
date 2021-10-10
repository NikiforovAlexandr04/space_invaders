class Scores:
    def __init__(self, score):
        self.score = score
        self.scores = []

    def print_score(self, score_count):
        """записывает очки в файл"""
        scores_file_read = open('scores.txt', 'r')
        scores = []
        self.score = score_count
        for line in scores_file_read:
            scores.append(int(line))
        scores_file_read.close()
        if len(scores) == 10 and self.score > scores[-1]:
            del scores[-1]
        scores.append(self.score)
        scores.sort()
        scores_file_write = open('scores.txt', 'w')
        scores_file_write.truncate()
        for score in scores:
            scores_file_write.write(str(score) + "\n")
        scores_file_write.close()

    def show_scores(self):
        """Показывает очки"""
        scores_file_read = open('scores.txt', 'r')
        self.scores = []
        for line in scores_file_read:
            self.scores.append(int(line))
        scores_file_read.close()
        self.scores.reverse()
        return self.scores
