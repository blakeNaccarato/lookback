"""Trello board model."""

# * Some skips for this auto-generated file
# pyright: reportMissingTypeArgument=false
# ruff: noqa: A003
# sourcery skip: name-type-suffix

# generated by datamodel-codegen:
#   filename:  c1tDMXSa.json
#   timestamp: 2022-12-12T23:01:38+00:00

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class PerBoard(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class PerCard(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class Attachments(BaseModel):
    per_board: PerBoard = Field(..., alias="perBoard")
    per_card: PerCard = Field(..., alias="perCard")


class TotalMembersPerBoard(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class TotalAccessRequestsPerBoard(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class Boards(BaseModel):
    total_members_per_board: TotalMembersPerBoard = Field(
        ..., alias="totalMembersPerBoard"
    )
    total_access_requests_per_board: TotalAccessRequestsPerBoard = Field(
        ..., alias="totalAccessRequestsPerBoard"
    )


class OpenPerBoard(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class OpenPerList(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class TotalPerBoard(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class TotalPerList(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class Cards(BaseModel):
    open_per_board: OpenPerBoard = Field(..., alias="openPerBoard")
    open_per_list: OpenPerList = Field(..., alias="openPerList")
    total_per_board: TotalPerBoard = Field(..., alias="totalPerBoard")
    total_per_list: TotalPerList = Field(..., alias="totalPerList")


class PerBoard1(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class PerCard1(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class Checklists(BaseModel):
    per_board: PerBoard1 = Field(..., alias="perBoard")
    per_card: PerCard1 = Field(..., alias="perCard")


class PerChecklist(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class CheckItems(BaseModel):
    per_checklist: PerChecklist = Field(..., alias="perChecklist")


class PerBoard2(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class CustomFields(BaseModel):
    per_board: PerBoard2 = Field(..., alias="perBoard")


class PerField(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class CustomFieldOptions(BaseModel):
    per_field: PerField = Field(..., alias="perField")


class PerBoard3(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class Labels(BaseModel):
    per_board: PerBoard3 = Field(..., alias="perBoard")


class OpenPerBoard1(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class TotalPerBoard1(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class Lists(BaseModel):
    open_per_board: OpenPerBoard1 = Field(..., alias="openPerBoard")
    total_per_board: TotalPerBoard1 = Field(..., alias="totalPerBoard")


class PerCard2(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class Stickers(BaseModel):
    per_card: PerCard2 = Field(..., alias="perCard")


class PerAction(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class UniquePerAction(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class Reactions(BaseModel):
    per_action: PerAction = Field(..., alias="perAction")
    unique_per_action: UniquePerAction = Field(..., alias="uniquePerAction")


class Limits(BaseModel):
    attachments: Attachments
    boards: Boards
    cards: Cards
    checklists: Checklists
    check_items: CheckItems = Field(..., alias="checkItems")
    custom_fields: CustomFields = Field(..., alias="customFields")
    custom_field_options: CustomFieldOptions = Field(..., alias="customFieldOptions")
    labels: Labels
    lists: Lists
    stickers: Stickers
    reactions: Reactions


class SwitcherView(BaseModel):
    _id: str
    view_type: str = Field(..., alias="viewType")
    enabled: bool


class BackgroundImageScaledItem(BaseModel):
    width: int
    height: int
    url: str


class Prefs(BaseModel):
    permission_level: str = Field(..., alias="permissionLevel")
    hide_votes: bool = Field(..., alias="hideVotes")
    voting: str
    comments: str
    invitations: str
    self_join: bool = Field(..., alias="selfJoin")
    card_covers: bool = Field(..., alias="cardCovers")
    is_template: bool = Field(..., alias="isTemplate")
    card_aging: str = Field(..., alias="cardAging")
    calendar_feed_enabled: bool = Field(..., alias="calendarFeedEnabled")
    hidden_plugin_board_buttons: list = Field(..., alias="hiddenPluginBoardButtons")
    switcher_views: list[SwitcherView] = Field(..., alias="switcherViews")
    background: str | None
    background_color: Any = Field(..., alias="backgroundColor")
    background_image: str = Field(..., alias="backgroundImage")
    background_image_scaled: list[BackgroundImageScaledItem] = Field(
        ..., alias="backgroundImageScaled"
    )
    background_tile: bool = Field(..., alias="backgroundTile")
    background_brightness: str = Field(..., alias="backgroundBrightness")
    background_bottom_color: str = Field(..., alias="backgroundBottomColor")
    background_top_color: str = Field(..., alias="backgroundTopColor")
    can_be_public: bool = Field(..., alias="canBePublic")
    can_be_enterprise: bool = Field(..., alias="canBeEnterprise")
    can_be_org: bool = Field(..., alias="canBeOrg")
    can_be_private: bool = Field(..., alias="canBePrivate")
    can_invite: bool = Field(..., alias="canInvite")


class LabelNames(BaseModel):
    green: str
    yellow: str
    orange: str
    red: str
    purple: str
    blue: str
    sky: str
    lime: str
    pink: str
    black: str
    green_dark: str
    yellow_dark: str
    orange_dark: str
    red_dark: str
    purple_dark: str
    blue_dark: str
    sky_dark: str
    lime_dark: str
    pink_dark: str
    black_dark: str
    green_light: str
    yellow_light: str
    orange_light: str
    red_light: str
    purple_light: str
    blue_light: str
    sky_light: str
    lime_light: str
    pink_light: str
    black_light: str


class Card(BaseModel):
    id: str
    name: str | None = None
    id_short: int = Field(..., alias="idShort")
    short_link: str = Field(..., alias="shortLink")
    desc: str | None = None
    pos: float | None = None
    id_labels: list[str] | None = Field(None, alias="idLabels")
    start: str | None = None
    id_list: str | None = Field(None, alias="idList")
    closed: bool | None = None
    due_reminder: int | None = Field(None, alias="dueReminder")
    due: str | None = None
    id_members: list[str] | None = Field(None, alias="idMembers")


class Prefs1(BaseModel):
    background: str | None


class Board(BaseModel):
    id: str
    name: str
    short_link: str = Field(..., alias="shortLink")
    prefs: Prefs1 | None = None


class Member(BaseModel):
    id: str
    name: str


class Attachment(BaseModel):
    id: str
    name: str
    url: str | None = None
    preview_url: str | None = Field(None, alias="previewUrl")
    preview_url2x: str | None = Field(None, alias="previewUrl2x")


class ListModel(BaseModel):
    id: str
    name: str | None = None
    pos: int | None = None


class Prefs2(BaseModel):
    background: str | None


class Old(BaseModel):
    desc: str | None = None
    pos: float | None = None
    id_labels: list[str] | None = Field(None, alias="idLabels")
    start: str | None = None
    id_list: str | None = Field(None, alias="idList")
    closed: bool | None = None
    name: str | None = None
    due_reminder: Any | None = Field(None, alias="dueReminder")
    due: str | None = None
    id_members: list[str] | None = Field(None, alias="idMembers")
    prefs: Prefs2 | None = None


class TextData(BaseModel):
    emoji: dict[str, Any]


class Checklist(BaseModel):
    id: str
    name: str


class TextData1(BaseModel):
    emoji: dict[str, Any]


class CheckItem(BaseModel):
    id: str
    name: str
    state: str
    text_data: TextData1 | None = Field(None, alias="textData")


class ListBefore(BaseModel):
    id: str
    name: str


class ListAfter(BaseModel):
    id: str
    name: str


class Prefs3(BaseModel):
    is_template: bool = Field(..., alias="isTemplate")


class BoardSource(BaseModel):
    id: str
    prefs: Prefs3 | None = None


class UsageBrackets(BaseModel):
    boards: int


class Icon(BaseModel):
    url: str


class Listing(BaseModel):
    name: str
    locale: str
    description: str
    overview: str


class HeroImageUrl(BaseModel):
    _id: str
    _2x: str = Field(..., alias="@2x")
    _1x: str = Field(..., alias="@1x")


class Plugin(BaseModel):
    id: str
    id_organization_owner: str = Field(..., alias="idOrganizationOwner")
    author: str
    capabilities: list[str]
    capabilities_options: list[str] = Field(..., alias="capabilitiesOptions")
    categories: list[str]
    iframe_connector_url: str = Field(..., alias="iframeConnectorUrl")
    name: str
    privacy_url: str = Field(..., alias="privacyUrl")
    public: bool
    moderated_state: Any = Field(..., alias="moderatedState")
    support_email: str = Field(..., alias="supportEmail")
    tags: list[str]
    is_compliant_with_privacy_standards: Any = Field(
        ..., alias="isCompliantWithPrivacyStandards"
    )
    usage_brackets: UsageBrackets = Field(..., alias="usageBrackets")
    claimed_domains: list[str] = Field(..., alias="claimedDomains")
    icon: Icon
    listing: Listing
    hero_image_url: HeroImageUrl | None = Field(None, alias="heroImageUrl")
    url: str | None = None


class BoardTarget(BaseModel):
    id: str


class Organization(BaseModel):
    id: str
    name: str


class Data(BaseModel):
    id_member: str | None = Field(None, alias="idMember")
    card: Card | None = None
    board: Board
    member: Member | None = None
    attachment: Attachment | None = None
    list: ListModel | None = None
    old: Old | None = None
    text: str = ""
    text_data: TextData | None = Field(None, alias="textData")
    date_last_edited: str | None = Field(None, alias="dateLastEdited")
    checklist: Checklist | None = None
    check_item: CheckItem | None = Field(None, alias="checkItem")
    list_before: ListBefore | None = Field(None, alias="listBefore")
    list_after: ListAfter | None = Field(None, alias="listAfter")
    deactivated: bool | None = None
    board_source: BoardSource | None = Field(None, alias="boardSource")
    plugin: Plugin | None = None
    board_target: BoardTarget | None = Field(None, alias="boardTarget")
    organization: Organization | None = None


class Icon1(BaseModel):
    url: str


class AppCreatorItem(BaseModel):
    id: str
    name: str | None = None
    icon: Icon1 | None = None


class PerAction1(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class UniquePerAction1(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class Reactions1(BaseModel):
    per_action: PerAction1 = Field(..., alias="perAction")
    unique_per_action: UniquePerAction1 = Field(..., alias="uniquePerAction")


class Limit(BaseModel):
    reactions: Reactions1


class NonPublic(BaseModel):
    full_name: str = Field(..., alias="fullName")
    initials: str
    avatar_hash: Any = Field(..., alias="avatarHash")


class Member1(BaseModel):
    id: str
    activity_blocked: bool = Field(..., alias="activityBlocked")
    avatar_hash: str = Field(..., alias="avatarHash")
    avatar_url: str = Field(..., alias="avatarUrl")
    full_name: str = Field(..., alias="fullName")
    id_member_referrer: Any = Field(..., alias="idMemberReferrer")
    initials: str
    non_public: NonPublic = Field(..., alias="nonPublic")
    non_public_available: bool = Field(..., alias="nonPublicAvailable")
    username: str


class NonPublic1(BaseModel):
    full_name: str = Field(..., alias="fullName")
    initials: str
    avatar_hash: Any = Field(..., alias="avatarHash")


class MemberCreator(BaseModel):
    id: str
    activity_blocked: bool = Field(..., alias="activityBlocked")
    avatar_hash: str = Field(..., alias="avatarHash")
    avatar_url: str = Field(..., alias="avatarUrl")
    full_name: str = Field(..., alias="fullName")
    id_member_referrer: Any = Field(..., alias="idMemberReferrer")
    initials: str
    non_public: NonPublic1 = Field(..., alias="nonPublic")
    non_public_available: bool = Field(..., alias="nonPublicAvailable")
    username: str


class Action(BaseModel):
    id: str
    id_member_creator: str = Field(..., alias="idMemberCreator")
    data: Data
    app_creator: AppCreatorItem | None = Field(..., alias="appCreator")
    type: str
    date: str
    limits: Limit | None
    member: Member1 | None = None
    member_creator: MemberCreator = Field(..., alias="memberCreator")


class Trello(BaseModel):
    board: int
    card: int


class AttachmentsByType(BaseModel):
    trello: Trello


class Badges(BaseModel):
    attachments_by_type: AttachmentsByType = Field(..., alias="attachmentsByType")
    location: bool
    votes: int
    viewing_member_voted: bool = Field(..., alias="viewingMemberVoted")
    subscribed: bool
    fogbugz: str
    check_items: int = Field(..., alias="checkItems")
    check_items_checked: int = Field(..., alias="checkItemsChecked")
    check_items_earliest_due: Any = Field(..., alias="checkItemsEarliestDue")
    comments: int
    attachments: int
    description: bool
    due: Any
    due_complete: bool = Field(..., alias="dueComplete")
    start: str | None


class DescData(BaseModel):
    emoji: dict[str, Any]


class Label(BaseModel):
    id: str
    id_board: str = Field(..., alias="idBoard")
    name: str
    color: str | None


class PerCard3(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class Attachments1(BaseModel):
    per_card: PerCard3 = Field(..., alias="perCard")


class PerCard4(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class Checklists1(BaseModel):
    per_card: PerCard4 = Field(..., alias="perCard")


class PerCard5(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class Stickers1(BaseModel):
    per_card: PerCard5 = Field(..., alias="perCard")


class Limits1(BaseModel):
    attachments: Attachments1
    checklists: Checklists1
    stickers: Stickers1


class ScaledItem(BaseModel):
    _id: str
    id: str
    scaled: bool
    url: str
    bytes: int
    height: int
    width: int


class Cover(BaseModel):
    id_attachment: str | None = Field(..., alias="idAttachment")
    color: Any
    id_uploaded_background: Any = Field(..., alias="idUploadedBackground")
    size: str
    brightness: str
    id_plugin: Any = Field(..., alias="idPlugin")
    scaled: list[ScaledItem] | None = None
    edge_color: str | None = Field(None, alias="edgeColor")


class Preview(BaseModel):
    _id: str
    id: str
    scaled: bool
    url: str
    bytes: int
    height: int
    width: int


class Attachment1(BaseModel):
    bytes: int | None
    date: str
    edge_color: str | None = Field(..., alias="edgeColor")
    id_member: str = Field(..., alias="idMember")
    is_upload: bool = Field(..., alias="isUpload")
    mime_type: str = Field(..., alias="mimeType")
    name: str
    previews: list[Preview]
    url: str
    pos: int
    file_name: str | None = Field(..., alias="fileName")
    id: str


class PluginDatum(BaseModel):
    id: str
    id_plugin: str = Field(..., alias="idPlugin")
    scope: str
    id_model: str = Field(..., alias="idModel")
    value: str
    access: str
    date_last_updated: str | None = Field(None, alias="dateLastUpdated")


class Card1(BaseModel):
    id: str
    address: Any
    badges: Badges
    check_item_states: Any = Field(..., alias="checkItemStates")
    closed: bool
    coordinates: Any
    creation_method: Any = Field(..., alias="creationMethod")
    due_complete: bool = Field(..., alias="dueComplete")
    date_last_activity: str = Field(..., alias="dateLastActivity")
    desc: str
    desc_data: DescData | None = Field(None, alias="descData")
    due: Any
    due_reminder: int | None = Field(..., alias="dueReminder")
    email: str
    id_board: str = Field(..., alias="idBoard")
    id_checklists: list[str] = Field(..., alias="idChecklists")
    id_labels: list[str] = Field(..., alias="idLabels")
    id_list: str = Field(..., alias="idList")
    id_members: list[str] = Field(..., alias="idMembers")
    id_members_voted: list = Field(..., alias="idMembersVoted")
    id_short: int = Field(..., alias="idShort")
    id_attachment_cover: str | None = Field(..., alias="idAttachmentCover")
    labels: list[Label]
    limits: Limits1
    location_name: Any = Field(..., alias="locationName")
    manual_cover_attachment: bool = Field(..., alias="manualCoverAttachment")
    name: str
    pos: float
    short_link: str = Field(..., alias="shortLink")
    short_url: str = Field(..., alias="shortUrl")
    static_map_url: Any = Field(..., alias="staticMapUrl")
    start: str | None
    subscribed: bool
    url: str
    cover: Cover
    is_template: bool = Field(..., alias="isTemplate")
    card_role: Any = Field(..., alias="cardRole")
    attachments: list[Attachment1]
    plugin_data: list[PluginDatum] = Field(..., alias="pluginData")
    custom_field_items: list = Field(..., alias="customFieldItems")


class Label1(BaseModel):
    id: str
    id_board: str = Field(..., alias="idBoard")
    name: str
    color: str | None


class OpenPerList1(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class TotalPerList1(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class Cards1(BaseModel):
    open_per_list: OpenPerList1 = Field(..., alias="openPerList")
    total_per_list: TotalPerList1 = Field(..., alias="totalPerList")


class Limits2(BaseModel):
    cards: Cards1


class List1(BaseModel):
    id: str
    name: str
    closed: bool
    id_board: str = Field(..., alias="idBoard")
    pos: int
    subscribed: bool
    soft_limit: Any = Field(..., alias="softLimit")
    limits: Limits2
    creation_method: Any = Field(..., alias="creationMethod")


class NonPublic2(BaseModel):
    full_name: str = Field(..., alias="fullName")
    initials: str
    avatar_hash: Any = Field(..., alias="avatarHash")


class Member2(BaseModel):
    id: str
    aa_id: str = Field(..., alias="aaId")
    activity_blocked: bool = Field(..., alias="activityBlocked")
    avatar_hash: str = Field(..., alias="avatarHash")
    avatar_url: str = Field(..., alias="avatarUrl")
    bio: str
    bio_data: Any = Field(..., alias="bioData")
    confirmed: bool
    full_name: str = Field(..., alias="fullName")
    id_enterprise: Any = Field(..., alias="idEnterprise")
    id_enterprises_deactivated: list = Field(..., alias="idEnterprisesDeactivated")
    id_member_referrer: Any = Field(..., alias="idMemberReferrer")
    id_prem_orgs_admin: list = Field(..., alias="idPremOrgsAdmin")
    initials: str
    member_type: str = Field(..., alias="memberType")
    non_public: NonPublic2 = Field(..., alias="nonPublic")
    non_public_available: bool = Field(..., alias="nonPublicAvailable")
    products: list
    url: str
    username: str
    status: str


class PerChecklist1(BaseModel):
    status: str
    disable_at: int = Field(..., alias="disableAt")
    warn_at: int = Field(..., alias="warnAt")


class CheckItems1(BaseModel):
    per_checklist: PerChecklist1 = Field(..., alias="perChecklist")


class Limits3(BaseModel):
    check_items: CheckItems1 = Field(..., alias="checkItems")


class NameData(BaseModel):
    emoji: dict[str, Any]


class CheckItem1(BaseModel):
    id: str
    name: str
    name_data: NameData | None = Field(None, alias="nameData")
    pos: float
    due: Any
    due_reminder: Any = Field(..., alias="dueReminder")
    id_member: Any = Field(..., alias="idMember")
    id_checklist: str = Field(..., alias="idChecklist")
    state: str


class Checklist1(BaseModel):
    id: str
    name: str
    id_board: str = Field(..., alias="idBoard")
    id_card: str = Field(..., alias="idCard")
    pos: int
    limits: Limits3
    creation_method: Any = Field(..., alias="creationMethod")
    check_items: list[CheckItem1] = Field(..., alias="checkItems")


class Membership(BaseModel):
    id_member: str = Field(..., alias="idMember")
    member_type: str = Field(..., alias="memberType")
    unconfirmed: bool
    deactivated: bool
    id: str


class PluginDatum1(BaseModel):
    id: str
    id_plugin: str = Field(..., alias="idPlugin")
    scope: str
    id_model: str = Field(..., alias="idModel")
    value: str
    access: str
    date_last_updated: str | None = Field(None, alias="dateLastUpdated")


class Model(BaseModel):
    id: str
    node_id: str = Field(..., alias="nodeId")
    name: str
    desc: str
    desc_data: Any = Field(..., alias="descData")
    closed: bool
    date_closed: Any = Field(..., alias="dateClosed")
    id_organization: str = Field(..., alias="idOrganization")
    id_enterprise: Any = Field(..., alias="idEnterprise")
    limits: Limits
    pinned: bool
    starred: bool
    url: str
    prefs: Prefs
    short_link: str = Field(..., alias="shortLink")
    subscribed: bool
    label_names: LabelNames = Field(..., alias="labelNames")
    power_ups: list = Field(..., alias="powerUps")
    date_last_activity: str = Field(..., alias="dateLastActivity")
    date_last_view: str = Field(..., alias="dateLastView")
    short_url: str = Field(..., alias="shortUrl")
    id_tags: list = Field(..., alias="idTags")
    date_plugin_disable: Any = Field(..., alias="datePluginDisable")
    creation_method: Any = Field(..., alias="creationMethod")
    ix_update: str = Field(..., alias="ixUpdate")
    template_gallery: Any = Field(..., alias="templateGallery")
    enterprise_owned: bool = Field(..., alias="enterpriseOwned")
    id_board_source: str | None = Field(None, alias="idBoardSource")
    premium_features: list[str] = Field(..., alias="premiumFeatures")
    id_member_creator: str | None = Field(None, alias="idMemberCreator")
    actions: list[Action]
    cards: list[Card1]
    labels: list[Label1]
    lists: list[List1]
    members: list[Member2]
    checklists: list[Checklist1]
    custom_fields: list = Field(..., alias="customFields")
    memberships: list[Membership]
    plugin_data: list[PluginDatum1] = Field(..., alias="pluginData")
