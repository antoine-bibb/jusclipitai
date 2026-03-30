from app.models.models import PlanTier, Subscription

PLAN_LIMITS = {
    PlanTier.FREE: {'uploads': 5, 'clips': 20},
    PlanTier.PRO: {'uploads': 30, 'clips': 150},
    PlanTier.BUSINESS: {'uploads': 200, 'clips': 1000},
}


def assert_upload_quota(subscription: Subscription) -> None:
    limits = PLAN_LIMITS[subscription.tier]
    if subscription.uploads_used_period >= limits['uploads']:
        raise ValueError('Upload quota exceeded for your plan')


def assert_clip_quota(subscription: Subscription) -> None:
    limits = PLAN_LIMITS[subscription.tier]
    if subscription.clips_used_period >= limits['clips']:
        raise ValueError('Clip render quota exceeded for your plan')
