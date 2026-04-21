from celery import shared_task


@shared_task
def log_sale_completed(sale_id: int) -> None:
    print(f'Sale {sale_id} completed successfully.')