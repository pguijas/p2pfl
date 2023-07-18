class NodeMessages:
    """
    ¿?¿?¿?¿?¿?¿?
    """

    BEAT = "beat"


class LearningNodeMessages(NodeMessages):
    """
    ¿?¿?¿?¿?¿?¿?
    """

    START_LEARNING = "start_learning"
    STOP_LEARNING = "stop_learning"
    MODEL_INITIALIZED = "model_initialized"
    MODELS_AGGREGATED = "models_aggregated"
    MODELS_READY = "models_ready"
    VOTE_TRAIN_SET = "vote_train_set"
    METRICS = "metrics"
