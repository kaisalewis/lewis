import hashlib
from typing import Any, Dict, Optional

from .models import AuditEvent


def _hash_payload(payload: Dict[str, Any]) -> str:
    m = hashlib.sha256()
    m.update(str(payload).encode("utf-8"))
    return m.hexdigest()


def append_audit_event(actor: str, action: str, context: Optional[Dict[str, Any]] = None) -> AuditEvent:
    context = context or {}
    last = AuditEvent.objects.order_by("-created_at").first()
    prev_hash = last.hash if last else ""
    payload = {"actor": actor, "action": action, "context": context, "prev_hash": prev_hash}
    current_hash = _hash_payload(payload)
    return AuditEvent.objects.create(
        actor=actor,
        action=action,
        context=context,
        prev_hash=prev_hash,
        hash=current_hash,
    )

