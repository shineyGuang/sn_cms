# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 16:52
# @Author  : 20019236
# @File    : response_code.py
# @Software: fastApi_CLI-master
class HTTP(object):
    HTTP_100_CONTINUE = 100  # 继续
    HTTP_101_SWITCHING_PROTOCOLS = 101  # 交换协议
    HTTP_200_OK = 200  # 查询请求成功
    HTTP_201_CREATED = 201  # 创建成功
    HTTP_202_ACCEPTED = 202  # 接受
    HTTP_203_NON_AUTHORITATIVE_INFORMATION = 203  # 非权威的信息
    HTTP_204_NO_CONTENT = 204  # 没有内容
    HTTP_205_RESET_CONTENT = 205  # 重置内容
    HTTP_206_PARTIAL_CONTENT = 206  # 部分内容
    HTTP_207_MULTI_STATUS = 207  # 多状态
    HTTP_300_MULTIPLE_CHOICES = 300  # 多个选择
    HTTP_301_MOVED_PERMANENTLY = 301  # 永久重定向
    HTTP_302_FOUND = 302  # 发现
    HTTP_303_SEE_OTHER = 303  # 重定向到其他
    HTTP_304_NOT_MODIFIED = 304  # 未修改
    HTTP_305_USE_PROXY = 305  # 使用代理
    HTTP_306_RESERVED = 306  # 未使用
    HTTP_307_TEMPORARY_REDIRECT = 307  # 临时重定向
    HTTP_400_BAD_REQUEST = 400  # 错误的请求
    HTTP_401_UNAUTHORIZED = 401  # 未经授权
    HTTP_402_PAYMENT_REQUIRED = 402  # 需要授权
    HTTP_403_FORBIDDEN = 403  # 禁止访问
    HTTP_404_NOT_FOUND = 404  # 没有找到
    HTTP_405_METHOD_NOT_ALLOWED = 405  # 方法不允许
    HTTP_406_NOT_ACCEPTABLE = 406  # 不可接受
    HTTP_407_PROXY_AUTHENTICATION_REQUIRED = 407  # 代理省份验证
    HTTP_408_REQUEST_TIMEOUT = 408  # 请求超时
    HTTP_409_CONFLICT = 409  # 资源冲突
    HTTP_410_GONE = 410  # 资源存在但是不可用了
    HTTP_411_LENGTH_REQUIRED = 411  # 没有定义content-length
    HTTP_412_PRECONDITION_FAILED = 412  # 前提条件失败
    HTTP_413_REQUEST_ENTITY_TOO_LARGE = 413  # 请求包太大
    HTTP_414_REQUEST_URI_TOO_LONG = 414  # 请求url太长
    HTTP_415_UNSUPPORTED_MEDIA_TYPE = 415  # 不支持的媒体类型
    HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE = 416  # 请求范围不足
    HTTP_417_EXPECTATION_FAILED = 417  # 预期失败
    HTTP_422_UNPROCESSABLE_ENTITY = 422  # 不可加工
    HTTP_423_LOCKED = 423  # 被锁定
    HTTP_424_FAILED_DEPENDENCY = 424  # 失败的依赖
    HTTP_425_TOO_EARLY = 425  # 言之过早
    HTTP_428_PRECONDITION_REQUIRED = 428  # 先决条件要求
    HTTP_429_TOO_MANY_REQUESTS = 429  # 请求太多
    HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE = 431  # 请求头字段太大
    HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS = 451  # 由于法律原因无法使用
    HTTP_500_INTERNAL_SERVER_ERROR = 500  # 服务器错误
    HTTP_501_NOT_IMPLEMENTED = 501  # 没有实现
    HTTP_502_BAD_GATEWAY = 502  # 网关错误
    HTTP_503_SERVICE_UNAVAILABLE = 503  # 服务不可用
    HTTP_504_GATEWAY_TIMEOUT = 504  # 网关超时
    HTTP_505_HTTP_VERSION_NOT_SUPPORTED = 505  # HTTP协议版本不支持
    HTTP_507_INSUFFICIENT_STORAGE = 507  # 存储不足
    HTTP_511_NETWORK_AUTHENTICATION_REQUIRED = 511  # 网络身份验证要求


class BUSINESS(object):
    # 认证相关
    INVALID_TOKEN = 20001  # 无效的token, 'Invalid token'
    ACCESS_TOKEN_EXPIRED = 20002  # access token过期, 'Access token expired'
    AUTHORIZATION_ERROR = 20004  # authorization字段错误, 'Authorization error'

    # 用户相关
    USER_NOT_EXIST = 40016  # 账户不存在, 'Account does not exist'
    USER_OR_PASSWORD_ERROR = 240017  # 账户或密码错误, 'Wrong account or password'
    ACCOUNT_LOCKED = 40018  # 账户已被锁定, 'Account has been locked'
    ACCOUNT_EXISTED = 40019  # 账号已被使用, 'Account existed'

    # 机器人相关
    ROBOT_CREATE_SUCCESS = 20021  # 机器人创建成功
    ROBOT_CREATE_FAILED = 40021  # 机器人创建失败
    ROBOT_NOT_FOUND_ERROR = 40001  # 找不到机器人
    ROBOT_EDIT_SUCCESS = 20031  # 更新机器人成功
    ROBOT_EDIT_FAILED = 40031  # 更新机器人失败
    ROBOT_DEL_SUCCESS = 20041  # 删除机器人成功
    ROBOT_DEL_FAILED = 40041  # 删除机器人失败
    # 类别相关
    CATEGORY_EDIT_FAILED = 40051  # 更新类别失败
    CATEGORY_NOT_FOUND = 40061  # 查找的类别不存在


class ResponseMessage(object):
    FormTagMakeErr = "Form表单生成失败"
    EnumTypeErr = "枚举类型错误"
    LoginSuccess = "登录成功"
    Success = "成功"
    DeleteSuccess = "删除成功"
    DeleteFail = "删除失败"
    Fail = "失败"
    NoResourceFound = "未找到资源"
    InvalidParameter = "参数无效"
    NotFondUserErr = "用户不存在"
    NotFondResourceErr = "数据库未找到资源"
    PasswordErr = "用户密码错误"
    IllegalLoginErr = "非法登录,请选择正确登录方式"
    # Token
    TokeninvalidErr = "传入无效的token,验证身份失败"
    TokenTimeOutErr = "token超时,请重新登录"
    TokenFlushSuccess = "刷新token成功"

    # 接口
    NoPermissionApiErr = "您没有权限访问该接口"
    InterfaceIsExistsErr = "当前接口已被占用,请更换"
    CreateInterfaceSuccess = "创建接口成功"
    InterfaceIsNotExistsErr = "当前接口不存在,请更换"
    EditInterfaceFail = "更改接口信息失败"
    EditInterfaceSuccess = "更改接口信息成功"
    DeleteInterfaceNotExists = "要删除的接口不存在"
    # 菜单
    MenuNameIsExistsErr = "菜单路由名称已被占用"
    MenuRouteIsExistsErr = "菜单路由路径已被占用"
    CreateMenuSuccess = "创建菜单成功"
    MenuParentIdIsNotExistsErr = "父菜单不存在"
    EditMenuFail = "更改菜单信息失败"
    EditMenuSuccess = "更改菜单信息成功"
    # 角色
    EditRoleFail = "更改角色信息失败"
    EditRoleSuccess = "更改角色信息成功"
    RoleParentIdIsNotExistsErr = "父角色id不存在"
    RoleIdIsNotExistsErr = "角色id不存在"
    RoleIdIsExistsErr = "角色id被占用,请更换"
    CreateRoleSuccess = "创建角色成功"
    GetRoleSuccess = "获取角色成功"
    CurrentRoleIsNotExistsErr = "当前角色不存在"
    # 数据
    DataRoleIsNotExistsErr = "当前角色没有分配数据权限"
    # 用户
    UserIsExistsErr = "用户名重复注册"
    PhoneIsExistsErr = "手机号重复注册"
    EmailIsExistsErr = "邮箱号重复注册"
    IdentityCodeIsExistsErr = "身份证号重复注册"
    CreateUserFail = "创建用户失败"
    UserRepeatLoginErr = "当前用户在其他地方登陆，请重新登陆"
    # 机器人
    CreateRobotSuccess = "创建机器人成功"
    CreateRobotFailed = "创建机器人失败"
    RobotIsExistErr = "机器人已存在"
    EditRobotSuccess = "更新机器人成功"
    EditRobotIsNotExistErr = "要更新的机器人不存在"
    DelRobotSuccess = "删除机器人成功"
    DelRobotFailed = "要删除的机器人已存在"
    # 类别
    CategoryNotExistErr = "要更新的类别不存在"
    CategoryIsExistErr = "要创建的类别已存在"
    DelCategorySuccess = "删除类别成功"
    DelCategoryFailed = "删除类别失败"


class ResponseCode(HTTP, BUSINESS):
    ...
