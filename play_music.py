import os
import pygame
import random
import time


class MusicPlayer:
    def __init__(self, directory, overlap_seconds=1):
        self.directory = directory
        self.overlap_seconds = overlap_seconds
        self.files = self.get_mp3_files()
        self.num_tracks = len(self.files)
        self.current_index = 0

        pygame.mixer.init()
        pygame.init()

        self.main_channel = pygame.mixer.Channel(0)
        self.next_channel = pygame.mixer.Channel(1)
        self.track_length = 0
        self.start_time = time.time()

    def get_mp3_files(self):
        return [os.path.join(self.directory, f) for f in os.listdir(self.directory) if f.endswith('.mp3')]

    def play_track(self, index, channel):
        file = self.files[index]
        sound = pygame.mixer.Sound(file)
        channel.play(sound)
        return sound.get_length()  # Возвращаем длину трека

    def start_playing(self):
        self.current_index = 0
        self.track_length = self.play_track(self.current_index, self.main_channel)
        self.start_time = time.time()

    def update_track(self):
        current_time = time.time()
        elapsed_time = current_time - self.start_time

        # Проверяем, если осталось меньше overlap_seconds до конца текущего трека, запускаем следующий
        if elapsed_time >= self.track_length - self.overlap_seconds:
            self.current_index = random.randint(0, self.num_tracks - 1)  # Обновляем индекс для следующего трека
            next_track_length = self.play_track(self.current_index, self.next_channel)

            # Обновляем каналы
            self.main_channel, self.next_channel = self.next_channel, self.main_channel
            self.track_length = next_track_length
            self.start_time = current_time  # Обновляем стартовое время для следующего трека

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        return True