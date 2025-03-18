from loguru import logger


def main():
    logger.debug('debug')
    logger.info('some info')
    logger.success('success')
    logger.warning('some warning')
    logger.error('some error')
    logger.critical('some critcal error')


if __name__ == "__main__":
    main()
