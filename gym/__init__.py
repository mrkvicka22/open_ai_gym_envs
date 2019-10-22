from gym.envs.registration import register

register(
    id='TicTacToe-v0',
    entry_point='tic_tac_toe.envs:TicTacToeEnviroment',
)
